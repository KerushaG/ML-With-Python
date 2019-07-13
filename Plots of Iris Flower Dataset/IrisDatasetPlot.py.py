#Data Science, Algorithms and Advanced Software Engineering, Task 15
#Kerusha Govender, 30.06.2019
#[A program that imports data for the iris flower and creates 12 subplots using 12 combinations of 2 of 4 of its features at a time, marking it as one of 3 classes 
#of iris flowers.]

from sklearn.datasets import load_iris
iris = load_iris()

print(type(iris))
print(iris['target_names'])
print(iris['data'])
print(iris['target'])
print(iris['DESCR'])
print(iris['feature_names']) #the iris data is organized accoring to 4 features.ie, 4 values makes up one record which is then given a
#target 0, 1 or 2, which represents the class of iris flower it is.
print(iris) 

import matplotlib.pyplot as plt #use to make plots
from sklearn.datasets import load_iris #use to work with data
import numpy as np #use for design
#On the figure we are dividing the space up into 12 blocks to create subplots
#4 is the rows, 3 is the columns, and the third number passed is the index number of where you will find each plot starting from top left corner to bottom right
fig = plt.figure() #the figure is a grid
ax1 = plt.subplot(4,3,1) #each block is now stored in variables
ax2 = plt.subplot(4,3,2)
ax3 = plt.subplot(4,3,3)
ax4 = plt.subplot(4,3,4)
ax5 = plt.subplot(4,3,5)
ax6 = plt.subplot(4,3,6)
ax7 = plt.subplot(4,3,7)
ax8 = plt.subplot(4,3,8)
ax9 = plt.subplot(4,3,9)
ax10 = plt.subplot(4,3,10)
ax11 = plt.subplot(4,3,11)
ax12 = plt.subplot(4,3,12)
    
iris = load_iris()
data = np.array(iris['data'])
#print(*data, sep = "\n") - when you print data you can see this As an array with 150 elements, and each of those elements is a record in itself containing 4 elements
#The 4 elements is 4 values each pertaining to one of the four features, the combo of values/features lead to the distinction of one of the 3 types of iris flowers
#So we have 150 different combinations of what could be classified as one of the 3 types of iris flowers
#print(len(data))
#print(*data[:,0]) - here we are slicing the data array to show 150 records but only the 1st element of each record so 150 of one set of values for one feature
#print(*data[:,1])
targets = np.array(iris['target']) #target=outcome=type of flower represented by 0, 1, 2
cd = {0:'r',1:'b',2:"g"} #assigning a colour to the above types; so the scatter points will be these colours
cols = np.array([cd[target] for target in targets])
#feature range: here we are using the variable blocks we created above to draw the scatter plots in using two features at a time and plotting the 150 records of data
#showing which flower it will most likely be according to the 2 features in each plot
#so we have 12 combinations of 4 features
#for scatter you pass values for x-axis and values for y axis and then a colour id
ax1.scatter(data[:,0], data[:,1], c = cols) 
ax2.scatter(data[:,0], data[:,2],c = cols)
ax3.scatter(data[:,0], data[:,3],c = cols)
ax4.scatter(data[:,1], data[:,0],c = cols)
ax5.scatter(data[:,1], data[:,2],c = cols)
ax6.scatter(data[:,1], data[:,3],c = cols)
ax7.scatter(data[:,2], data[:,0], c = cols) 
ax8.scatter(data[:,2], data[:,1],c = cols)
ax9.scatter(data[:,2], data[:,3],c = cols)
ax10.scatter(data[:,3], data[:,0],c = cols)
ax11.scatter(data[:,3], data[:,1],c = cols)
ax12.scatter(data[:,3], data[:,2],c = cols)
#compiles and shows the figure with final info:
plt.show()
