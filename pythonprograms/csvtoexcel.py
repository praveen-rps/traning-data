import csv
from openpyxl import Workbook

# to read the data from csv file
#csv_file =  input("Enter the filename: ")
csv_file="results.csv"
data = []
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# write the data to excel file
#excel_file = input("Enter your excel file to write")
excel_file = "result.xlsx"
workbook = Workbook()
worksheet = workbook.active
worksheet.title = "Results"

for row in data:
    worksheet.append(row)

workbook.save(excel_file)
print(f"Data read from {csv_file} file and written to {excel_file}")

