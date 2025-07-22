import re

text1 = "India,Japan,China,Nepal"
text2 = "TS30AP20TN40"
result1 = re.split(r",", text1)
result2 = re.split(r"\d+",text2)
print(result1)
print(result2)
