# Read data from keyboard and send it to file

filename = input("Enter file name to write data")

with open(filename,"a") as fp:
    print("Enter the data ")
    while True:
        line = input()
        if line.lower() == "exit":
            break
        fp.write(line+"\n")

print("Data written to file successfully...!")
