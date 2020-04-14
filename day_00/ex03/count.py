import sys
import string

def text_analyser(text={}):
    upper = lower = space = punct = nb_char = 0
    if text is text_analyser.__defaults__[0]:
        text = input("What is the text to analyze ?")
    for char in text:
        if (char.isupper()):
            upper += 1
        if (char.islower()):
            lower += 1
        if (char == ' '):
            space += 1
        if char in string.punctuation:
            punct += 1
        nb_char += 1
    print("The text contains", nb_char, "characters:\n\n", "-", upper,
    "upper letters\n\n", "-", lower, "lower letters\n\n", "-", punct,
    "punctuation marks\n\n", "-", space, "spaces")
