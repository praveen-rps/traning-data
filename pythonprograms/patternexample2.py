import re

string1 = "Python is a best general purpose language"
string2 = "Python version 3 java version 22 devops version 4"
string3 = "Alice and Bob are living in California and Dallas"
string4 = "playing, singing and dancing are best forms of refreshments for the body"
string5 = "#python is good for #AI and #datascience, also for #statical processing"
string6 = "my email id is praveen@gmail.com and lives in #703 flat(my home)"

pattern1 = r"\b\w+\b" # This pattern is used to get the words
pattern2 = r"\d+" # This pattern is used to extract all the numbers
pattern3 = r"\b[A-Z][a-z]*\b" # this pattern in used to check the words with upper case
pattern4 = r"\b\w+ing\b" # this pattern is used to check the words ending with ing
pattern5 = r"#\w+" #this pattern is uded to get the hashtag words
pattern6 = r"[^\w\s]"

words = re.findall(pattern1,string1)
nums = re.findall(pattern2,string2)
uppercasewords = re.findall(pattern3,string3)
ingwords = re.findall(pattern4,string4)
hashtagwords = re.findall(pattern5,string5)
specialwords = re.findall(pattern6,string6)

print(words)
print(nums)
print(uppercasewords)
print(ingwords)
print(hashtagwords)
print(specialwords)

