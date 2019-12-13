#!/usr/bin/python3
#very simple wordlist generator
import itertools as itr

# comma separated words without spaces, example: test1,test2,test3,$,%,34
words = input(">>> ").split(",")
# starting fixed word, if none leave empty and press enter
fixedWord = input(">>> ")

file = open('wordlist.txt', 'w')

try:
	count = 0
	for r in range(2,len(words)+1):
		for i in list(itr.permutations(words, r)):
			file.write(fixedWord + ''.join(i) + "\n")
			count += 1
	print("Generated " + str(count) + " possible passwords in wordlist.txt")
finally:
	file.close()



