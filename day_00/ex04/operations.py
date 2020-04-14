import sys

def print_usage():
    print("Usage: python operation.py <nb1><nb2>\nExample:\n\tpython operation.py 10 3")

if len(sys.argv) < 3:
    print("InputError: not enough argument\n")
    print_usage()
elif len(sys.argv) > 3:
    print("InputError: too many argument\n")
    print_usage()
else:
    for elem in sys.argv[1:]:
        if not elem.isdigit():
            print("InputError: only numbers\n")
            print_usage()
            sys.exit(0)
print("Sum:         ", int(sys.argv[1]) + int(sys.argv[2]))
print("Difference:  ", int(sys.argv[1]) - int(sys.argv[2]))
print("Product:     ", int(sys.argv[1]) * int(sys.argv[2]))
if int(sys.argv[2]) != 0:
    print("Quotient:    ", int(sys.argv[1]) / int(sys.argv[2]))
else:
    print("ERROR (div by zero)")
if int(sys.argv[2]) != 0:
    print("Remainder:   ", int(sys.argv[1]) % int(sys.argv[2]))
else:
    print("ERROR (modulo by zero)")
