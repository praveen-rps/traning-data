import re
text = "Welcome to python programing in 2025 session for python full stack program"
str = "My name is praveen and my email  is praveen@rpsconsulting.com"


match1 = re.search("python",text)
match2 = re.search(r"(\w+)@(\w+)\.com", str)

if match1:
    print("Matched text is : ", match1.group())
    print("Start Index :", match1.start())
    print("End index : ", match1.end())
else:
    print("No match")


if match2:
    print("Full match: ", match2.group(0))
    print("username part", match2.group(1))
    print("domain   part", match2.group(2))
else:
    print("NO Match")


data= "Welcome to RPS Technolgoies"
match4 = re.search(r"RPS",data)
if match4:
    print("Span : ", match4.span())
else:
    print("No match ")
