import sys
import string

if (len(sys.argv) != 3): print("ERROR")
if sys.argv[1].isprintable() is False or sys.argv[1].isdecimal() or sys.argv[2].isdecimal() is False:
    print("ERROR")

lst = [word.translate(str.maketrans('','',string.punctuation)) for word in sys.argv[1].split(" ") if len(word) > int(sys.argv[2])]

print(lst)


