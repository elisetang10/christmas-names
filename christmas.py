import random
adjectives = open("adjectives.txt","r")
adjectivelist = []
while(adjectives.readline()!=""):
    split = adjectives.readline().split("\n")
    adjectivelist.append(split[0])
names = open("names.txt","r")
characters = []
while(names.readline()!=""):
    split = names.readline().split("\n")
    characters.append(split[0])
adjectives.close()
names.close()
title = random.choice(adjectivelist)
n = random.choice(characters)
print("christmas is coming!!!!\n")
print("generate a random christmas name for yourself.")
print(f"your christmas name is: {title} {n}")