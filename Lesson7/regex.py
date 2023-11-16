import re
def stripfn(phrase,remv):
    ask= input("Y/N to strip a particular word")
    if ask.lower()=="N":
        return phrase.strip()
    else: 
        remv= input("what to remove char ")
        phraseregex= re.compile(remv)
        return phraseregex.sub("", phrase)
remv= ""
phrase= input("Enter a string: ")
print(stripfn(phrase, remv))