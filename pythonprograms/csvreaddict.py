import csv

with open("results.csv","r") as fp:
    dictdata = csv.DictReader(fp);
    for data in dictdata:
        print(f"{data['Name']} has scored below Marks" )
        print(f"Maths : {data['Maths']}")
        print(f"Science : {data['Science']}")
        print(f"Social : {data['Social']}")


