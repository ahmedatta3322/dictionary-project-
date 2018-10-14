import json
import keyword
from difflib import get_close_matches
data = json.load(open('data.json'))


def find(w):
    w = w.lower()
    if data.get(w) != None:
        return "The word you are searching for is : ", data[w]
    elif get_close_matches(w, data) != None:
        print("did you mean one of them ? if yes please enter it correctly ",
              get_close_matches(w, data, n=1))
        return(data[input()])
    else:
        return "please try again and enter vaild data"

output = find((input("please enter the word you want to search : ")))
if type(output) == list :
    for word in output:
        print(word)


#print(find((input("please enter the word you want to search : "))))
