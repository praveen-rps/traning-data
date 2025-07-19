import csv

with open("employees.csv","r") as csvfile:
   reader = csv.reader(csvfile) # reader method reads all the csv data and return in the list format
   reader.__next__()
   for row in reader:
        print(row)