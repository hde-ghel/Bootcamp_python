import sys

string = ""
for arg in sys.argv[1:]:
    string = string + " " + arg
string = string[1:].swapcase()

print(string[::-1])
