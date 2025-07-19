import csv

data = [
    ["Name","Maths","Science","Social"],
    ["Alice",85,79,84],
    ["Bob",56,64,69],
    ["Charlie",90,92,91],
    ["David",75,79,71]
]

with open('results.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("Data written to csv file...!")