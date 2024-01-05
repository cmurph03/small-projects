# Originally written in June 2020
# This program is used for cell typing HiPlex RNAscope data based on 
# the presence of Gfap, Rbfox3, and Aif1 for use in CNS samples.
# It was made for a specific project with a specific file format
# where columns C,D,and E were Gfap, Aif1, and Rbfox3 respectively


import xlsxwriter
import pandas as pd

newColumn=[] #create a list for the new column that labels the cell type

readfile=input('Input CSV file: ')
outputfile=input('Name of output file: ')

outputfile=outputfile + '.xlsx'
wb=xlsxwriter.Workbook(outputfile) #create the new excel doc
sheet1=wb.add_worksheet('Sheet 1') #create the worksheet for the data

row=0


#this reads the file line by line (or row by row)
with open(readfile) as data:
    for line in data:
        entry=line.rstrip('\n') #remove the new tab at end of row
        info=entry.split(',') #remove the commas from the row


        #copy existing data to new file
        col=0  #need to go over all columns so this has to be reset to 0 as the
                #rows are looped though using line in data
        for j in range(len(info)):
            try:                #the try/except clause converts all the numbers stored
                                #as strings to actual numbers in the excel sheet
                mean=float(info[col])
                sheet1.write(row,col,mean)
            except ValueError:
                sheet1.write(row,col,info[col])
            col+=1      #loop through the columns
        row+=1
        
        #the first row is the title row, so identify that and append the label for
        #the new column added to the end of the row
        if info[0]=='Label':
            newColumn.append('cell type')
        else:           #if not on the first row, convert the desired data to numbers
            gfap=float(info[2])
            Aif1=float(info[3])
            Rbfox3=float(info[4])

            #once converted to numbers, evaluate the cell types
            #the cell type is determined by finding the largest by at least 1
            #(aka it has to be greater than the other 2 to determine the cell type)
            if gfap==Aif1==Rbfox3==0:
                newColumn.append('none')
            elif gfap-Aif1>1 and gfap-Rbfox3>1:
                newColumn.append('astrocyte')
            elif Aif1-gfap>1 and Aif1-Rbfox3>1:
                newColumn.append('microglia')
            elif Rbfox3-Aif1>1 and Rbfox3-gfap>1:
                newColumn.append('neuron')
            else:
                newColumn.append('undetermined')


#add the new column to the worksheet
for row in range(len(newColumn)):
    sheet1.write(row,20,newColumn[row])
    
wb.close()

data_xls = pd.read_excel(outputfile, dtype=str, index_col=None)
data_xls.to_csv(outputfile + '.csv', encoding='utf-8', index=False)
