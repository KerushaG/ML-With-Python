#Data Science, Algorithms and Advanced Software Engineering, Task 16.2
#Kerusha Govender, 02.06.2019
#Program that finds the best line of fit and produces a figure with testing and training data from a specified amount of records in a diabetes data set,
#using only one feature.
#################################################################################
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
import statistics as stats
from sklearn import linear_model 

#This method takes in data set for the x axis and for the y axis and calculates the m and b for the formula y = mx +b, which produces the line of best fit
def line_of_best_fit(data_x, data_y):
    mean_x = np.mean(data_x) #working out the mean of the x and y data sets and storing it in variables
    mean_y = np.mean(data_y)
    m = len(data_x) #for the range
    numer = 0
    denom = 0
    for i in range(m):
        numer += (data_x[i] - mean_x) * (data_y[i] - mean_y)
        denom += (data_x[i] - mean_x) ** 2
    m = numer / denom
    b = mean_y - (m * mean_x)
    return m, b
    
diabetes_data = load_diabetes() #load 442 records consisting of data for 10 features
bmi_feature = diabetes_data.data[:,np.newaxis, 2] #choosing one feature, BMI. Selecting only one column of [2] from all records
#data split into training and testing data
#First 80 samples used for training
dx_train = bmi_feature[:-80] 
dy_train = diabetes_data.target[:-80]
#last 20 samples used for testing
dx_test = bmi_feature[-20:]
dy_test = diabetes_data.target[-20:] 
#send training data to the method 
m, b = line_of_best_fit(dx_train, dy_train)
#applying y = mx + b to each value in the BMI test array and storing them in a new array to plot the line
array_line = []
for x in dx_test:
    array_line.append((m*x)+b)
#scatter implements the data on the figure and plot draws the line, legend creates a box showing the labels for the coloured data
plt.scatter(dx_train, dy_train, c = 'r', label = 'Training Data') 
plt.scatter(dx_test, dy_test, c = 'g', label = 'Testing Data') 
plt.plot(dx_test, array_line, c = 'b', label = 'Line of Best Fit') 
plt.xlabel('BMI')
plt.ylabel('Indication of Diabetes by way of Glucose levels')
plt.legend()
plt.show()
