

with open("output.txt","w") as fp:
    fp.write("Java is object oriented language\n")
    fp.write("Java is now functional oriented language also\n")
    fp.write("Java can be used for many other frameworks to implement\n")

lines = [
    "Spirng is written using java\n", "Springboot is also drawn from spring\n",
    "Andriod is also written using Java\n"
]

with open("output.txt","a") as fp:
    fp.writelines(lines)

print("Data written to the output.txt file")
