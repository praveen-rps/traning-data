import csv
data = []

with open("results2.csv","r") as inputdata:
    reader = csv.DictReader(inputdata)

    for row in reader:
        name = row["Name"]
        maths = row["Maths"]
        science = row["Science"]
        social = row["Social"]
        total = maths + science + social
        avg = round( (total/3), 2)
        data.append({
            "Name": name,
            "Maths": maths,
            "Science": science,
            "Social": social,
            "Total": total,
            "Avg": avg
        })


