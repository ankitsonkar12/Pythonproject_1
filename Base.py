import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

'''
data = json.load(open("data.json"))
word = input("Please type your word: ")
#print(data.keys())
print(data[word])

data = json.load(open("data.json"))
word = input("Please enter your data: ")
w = word.lower()
def found_word(w):
    if SequenceMatcher.(None,w,data.keys())
        return "are you looking for {}".format(s)
def transform(w):
    if w in data.keys():
        return data[w] 
    else:
        return "Invalid input"
print (found_word(word))        
#print(transform(w))
'''
file = json.load(open("data.json"))
#print(file.keys())
word  = input("Please enter your words : ")

def transform(word):
    word = word.lower()
    if word in (file.keys()):
        return file[word]
    elif word.title() in (file.keys()):
        return file[word.title()]   
    elif word.upper() in (file.keys()):
        return file[word.upper()]    
    elif len(get_close_matches(word, file.keys())) > 0:
        yn = input("Did you mean %s ? If yes press y or n for exit: " % get_close_matches(word, file.keys())[0])
        if yn == "y":
            return file[get_close_matches(word, file.keys())[0]]
        else:
            return "okay"    
        return "Did You mean %s " % get_close_matches(word , file.keys())[0]

    else:
        return "Invalid Input"    
output = transform(word)

if type(output) == list:
    for i in output:
        print(i)

else:
    print(output)