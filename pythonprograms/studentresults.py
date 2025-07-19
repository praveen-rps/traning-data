import csv
data = []

with open("results2.csv","r") as inputdata:
    reader = csv.DictReader(inputdata)

    for row in reader:
        name = row["Name"]
        maths = int(row["Maths"])
        science = int(row["Science"])
        social = int(row["Social"])
        total = maths + science + social
        avg = total/3
        data.append({
            "Name": name,
            "Maths": maths,
            "Science": science,
            "Social": social,
            "Total": total,
            "Avg": round(avg, 2),
        })
    fields = ["Name","Maths","Science","Social","Total","Avg"]

    with open("studentresults.csv","w") as output:
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
    print("Results are proessed successfully")

