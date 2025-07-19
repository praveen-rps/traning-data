import csv

data = [
    {"Name":"Arun", "Maths":87,"Science":86,"Social":90},
    {"Name":"Mahesh", "Maths":52,"Science":58,"Social":60},
    {"Name":"Kiran", "Maths":40,"Science":56,"Social":50},
    {"Name":"Mohan", "Maths":70,"Science":74,"Social":75},
    {"Name":"Prakash", "Maths":91,"Science":90,"Social":88}
]
fields = ["Name","Maths","Science","Social"]
with open("results2.csv","w") as fp:
    writer = csv.DictWriter(fp,fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
print("The data has been written to file")