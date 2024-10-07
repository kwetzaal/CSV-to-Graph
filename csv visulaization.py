
import csv
import matplotlib.pyplot as plt
import numpy as np

def column_to_array(filename, column_name):
    #Extracts a single column from a CSV file and returns it as a NumPy array
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        column_data = [row[column_name] for row in reader]
    return np.array(column_data)


str_filename = input("Name of CSV file (no quotations): ")

###open file and intitialize csv reader###
fh = open(str_filename)
csv_reader = csv.reader(fh)

ind = input("Name of Independent(x-axis) column in CSV file: ")
x = column_to_array(str_filename, ind)
dep = input("Name of dependent(y-axis) column in CSV file: ")
y = column_to_array(str_filename, dep)

print(x)
print(y)

#allows user to craete axis/graph labels
xlabel = input("X axis label: ")
ylabel = input("Y axis label: ")
title = input("Graph title: ")

#cehcks for errors in the independent data
error = input("Are there errors in the data (Y or N): ")
if error == "Y":
    error_in = input("What are errors displayed as in CSV (ie. NaN): ")
    error_out = float(input("How should errors be displayed in teh data (must be an number): "))

    #counting number of errors in the independent data
    counter = -1
    for i in y:
        counter += 1
        if i == "error_in":
            y[counter] = error_out


#changes entries into graphable values
x = [float(i) for i in x]
y = [float(i) for i in y]

#plots data
plt.scatter(x, y)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

plt.grid()

plt.show()

