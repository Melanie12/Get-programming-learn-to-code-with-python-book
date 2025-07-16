#You're playing a simpler version of Scrabble with your kids. The kids have been winning most games so far, and you realize it's because you aren't picking the best word from the given tiles. 
#You decide that you need a bit of help in the form of a computer program.

#The Problem
#Write a program that can tell you words that you can form from a set of tiles; the set of all valid words is a subset of all the English words [in this case, only words related to art].
#When dealing with choosing the best word from the given tiles, here are some details to remember:
#All valid words related to art are given to you as a string, each word separated by a newline.
#The string organizes the words by length, shortest to longest. 
#All valid words contain only letters in the alphabet [no spaces, hyphens, or special symbols]. For example, art, hue, oil, ink... 
#The number of tiles you get can vary; it's not a fixed number.
#Letters on tiles don't have point values; they are all worth the same. 
#The tiles you get are given as a string. For example, tiles ="hijklmnop". 
#Report all valid words you can form with your tiles in a tuple of strings ; for example ('ink','oil,'kiln').


#Valid words as a big string
words ="""
art 
hue 
ink
oil
clay
film
kiln
crosshatching"""

#print(words)
#print(type(words))

tiles = "hijklmnop"
#print(tiles)
#print(type(tiles))

#ink, kiln, oil this should be the input!

#My Code

#first I need to create a tuple of strings

valid_words=tuple(words.split("\n"))
print (valid_words) #creates a tuples of single characters, spaces and \n
#here I succeeded the objective to create a tuple of strings



#Book correction

all_valid_words=() #Empty tuple for all valid words
start = 0 #initializes a pointer to the beginning of index search
end = 0 #initializes a pointer to the end of index search
found_words=() #empty tuple for words found in tiles

for char in words: #iterates through every character
    if char=="\n": #checks whether the character is a newline
        all_valid_words=all_valid_words+(words[start:end],) #adds singleton tuple to current all valid words tuple
        start = end + 1 #moves start and end pointers to start of next word.
        end = end + 1
    else:
        end = end + 1 #moves only end pointer

print(all_valid_words)

for word in all_valid_words: #looks for every valid words
    tiles_left=tiles #tiles_left deals with duplicate tiles
    for letter in word: #looks at every letter in a valid word
        if letter not in tiles_left: #stops looking if letter not in tiles_left
            break
        else:
            index=tiles_left.find(letter) #finds position of letters in tiles_left
            tiles_left=tiles_left[:index]+tiles_left[index+1:] #removes letter and makes a new tiles_left
    if len(word) == len(tiles) - len(tiles_left): #checks whether found entire word
        found_words=found_words +(word,) #adds word to found_words
print(found_words)