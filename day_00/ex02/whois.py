import sys


if(len(sys.argv) == 1):
    sys.exit(0)
if (len(sys.argv) == 2 and sys.argv[1].isdigit()):
    nb = int(sys.argv[1])
    if (nb == 0):
        print("I'm Zero.")
    elif ((nb % 2) == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
else:
    print("ERROR")
