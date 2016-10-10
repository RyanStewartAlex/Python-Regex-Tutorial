r'''
Created by @RyanStewartAlex of http://www.ryanstewart.pw/

Purpose: Teach python regex and how regex works generally

What is Regex?
	- Regular Expressions
	- string searching and munip 
	- a lot more efficient and powerful than string subs and string searching manually

Commonly used re functions:
	- re.split(): splits an array where the pattern is found
	- re.match(): see if expression matches ENTIRE string
	- re.search(): see if match anywhere in string
	- re.findall(): returns every instance of a found pattern

Commonly used regex indentifiers:
	- \d: any number
	- \D: anything but a number
	- \s: space
	- \S: anything but a space
	- \w: any character
	- \W: anything but a character
	- . : any character except new line
	- \.: decimal point
	- \b: whitespace around words

Commonly used regex modifiers:
	- {1}: exactly one of the item
	- {1,3}: between one and three occurances (**Can't be a space in here!)
	- +: 1 or more
	- ?: 0 or 1
	- *: 0 or more
	- $: match end of a string
	- ^: match at the beginning of a string
	- [^]: not. i.e, [^c-d]ats removes cats and dats
	- |: either or. ex: \d{1, 3}|\w{1, 3}
	- [A-Za-z0-9]: range
	- ?!: negative look ahead. Means the stuff after it is excluded

Commonly used whitespace characters:
	- \n: new line
	- \s: space
	- \t: tab
	- \e: escape
	- \f: form feed
	- \r carriage return

Commonly used regex flags (arguments for the regex):
	- re.I: ignore casing
	- re.M: multilined
'''
import re, urllib2

string = "This is the string that will be BIGsBIG munipulated througout this file 1 2 3 meme 4 10, 5000, 14, 15, 9"


def getTitle(url):
	response = urllib2.urlopen("http://www." + url).read()
	data = re.findall(r'<title>(.+?)</title>', response) #the grouping exludes "<title>" and "</title>" from the result"
	print(data)


websites = ["google.com", "youtube.com", "ryanstewart.pw", "niil.me", "minecraft.net", "apple.com", "bbc.com", "fakeaddress.com"]
for w in websites:
	try:
		getTitle(w)
	except:
		pass #if it catches an exception just let it go

def getTwoOrLargerDigit():
	print(re.findall(r'\d{2,4}', string))

getTwoOrLargerDigit()


def getCapitalizedWords():
	print(re.findall(r'[A-Z]{1}[a-z]+', string))

getCapitalizedWords()


def get3Cap1Small3Cap():
	print(re.findall(r'[A-Z]{3}[a-z]{1}[A-Z]{3}', string))

get3Cap1Small3Cap()


def getMunipulate():
	print(re.findall(r'munipul[ae]ted', string, re.I)) #finds regardless if spelled "munipulated" or "munipuleted"

getMunipulate()


def getWordBeforeNumber():
	print(re.findall(r'[a-z]+\s\d+', string))

getWordBeforeNumber()


def everyWordExceptMeme():
	print(re.findall(r'\b(?!meme\b)\w+', string))

#everyWordExceptMeme()