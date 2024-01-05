from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

readfile=input('Input CSV file: ')

marker1=input('First marker to plot: ')
marker2=input('Second marker to plot: ')
marker3=input('Third marker to plot: ')

X=[] #create the lists for the axes
Y=[]
Z=[]

fig = plt.figure() #create the plot
ax = fig.add_subplot(111, projection='3d')

#this reads the file line by line (or row by row)
with open(readfile) as data:
    for line in data:
        entry=line.rstrip('\n') #remove the new tab at end of row
        info=entry.split(',') #remove the commas from the row

        #use the first row to find the index of the desired markers in the table
        if info[0]=='Label':
            x=info.index(marker1)
            y=info.index(marker2)
            z=info.index(marker3)
        else:       #Add the values to the list for each axis
            X.append(float(info[x]))
            Y.append(float(info[y]))
            Z.append(float(info[z]))

ax.scatter(X,Y,Z, c='r', marker='o')

ax.set_xlabel(marker1)
ax.set_ylabel(marker2)
ax.set_zlabel(marker3)

plt.show()
