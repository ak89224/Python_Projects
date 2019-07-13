'''
Created on Mar 02, 2019

@author: Abhishek.kumar
'''

import json
from difflib import *


Dictonary = json.load(open("SortedDictonary.json"))


def meaning(word):
    if word in Dictonary:
        return Dictonary[word]
    elif word.title() in Dictonary:
        return Dictonary[word.title()]
    elif word.upper() in Dictonary:
        return Dictonary[word.upper()]
    else:
        return suggestion(word)


def suggestion(word):
    if get_close_matches(word,Dictonary.keys(),n=1,cutoff=0.8):
        suggestion = sorted(get_close_matches(word, Dictonary.keys(), n=3, cutoff=0.8))[0]
        choice = input("Did you mean %s instead ? [Press Y/N]: " % suggestion).casefold()
        if choice == 'y':
            return meaning(suggestion)
        elif choice == 'n':
            return "Then the initial input Word doesn't exits, Please double check"
        return "Sorry!!!, We didn't understand your input."
    else:
        return "Word doesn't exits, Please double check"


word = input("Enter the word: ").casefold()

print(meaning(word))
