import json

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return iword + " not found in dictionary."

iword = input("Enter a word: ")

print(translate(iword))
