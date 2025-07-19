# This program will read data from a file and send it to monitor
# to open the file for read purpose
fp = open("data.txt","r")
try:
   # content = fp.read()
   #print(content)
   #line1 = fp.readline()
   #line2 = fp.readline()
   #print(line1)
   #print(line2)
   lines = fp.readlines()
   print(type(lines))
   for line in lines:
       print(line)

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)





# close the file pointer