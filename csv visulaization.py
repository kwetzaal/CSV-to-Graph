import sys

import csv
import matplotlib.pyplot as plt
import numpy as np

def column_to_array(filename, column_name):
    #Extracts a single column from a CSV file and returns it as a NumPy array
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        column_data = [row[column_name] for row in reader]
    return np.array(column_data)


#str_filename = input("Path to CSV file (no quotations): ")
str_filename = 'mars_weather.csv'

###open file and intitialize csv reader###
fh = open(str_filename)
csv_reader = csv.reader(fh)

#ind = input("Name of Independent(x-axis) column in CSV file: ")
ind = "sol"
x = column_to_array(str_filename, ind)
x = x[::-1]
dep = input("Name of dependent(y-axis) column in CSV file: ")
#dep = "pressure"
y = column_to_array(str_filename, dep)
y = y[::-1]

print(x)
print(y)

#allows user to craete axis/graph labels
xlabel = "Martian Days Elapsed (sol)"
#xlabel = input("X axis label: ")
ylabel = input("Y axis label: ")
title = input("Graph title: ")

#xlim = list(input("Limit on x-axis in the form (a, b) (input (0, 0) if no limits): "))
#ylim = list(input ("Limit on y-axis in the form (a, b) (input (0, 0) of no limits): "))

#counting number of errors in the pressure data
counter = -1
for i in y:
    counter += 1
    if i == "NaN":
        y[counter] = -100


#changes entries into graphable values
x = [float(i) for i in x]
y = [float(i) for i in y]

plt.scatter(x, y)
#if xlim != (0, 0):
#    plt.xlim(xlim)
#if ylim != (0, 0):
#    plt.ylim(ylim)

plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

'''plt.xlabel("x")
plt.ylabel("y")
plt.title("title")'''

plt.grid()

plt.show()

