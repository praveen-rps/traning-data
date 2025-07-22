import re
def count_words_numbers_from_file(filename):
    try:
        with open(filename,'r') as f:
            contents = f.read()
            wordpattern = r"\b\w+\b"
            words = re.findall(wordpattern, contents)
            wordcount = len(words)

            special_chars = r"[^a-zA-Z0-9\s]"
            specialchars = re.findall(special_chars, contents)
            specialcharcount = len(specialchars)

            digit_chars = r"\d"
            digitchars = re.findall(digit_chars, contents)
            digitcount = len(digitchars)

            print("The number of words : ", wordcount)
            print("The number of special chars : ", specialcharcount)
            print("The number of digit chars : ", digitcount)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":

    filename = input("Enter the file name")
    count_words_numbers_from_file(filename)