t = (19, 42, 21)

string, nb = "", 0

for each in t:
    string += str(each) + ", "
    nb += 1
string = string[:-2]
print("The", nb, "numbers are:", string)
