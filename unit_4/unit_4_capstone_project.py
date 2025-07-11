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
words ="""art 
hue 
ink
oil
clay
film
kiln
crosshatching
"""


tiles = "hijklmnop"

#ink, kiln, oil

valid_list = []

for i in tiles:
    if i in words:
        valid_list.append(i)


print(valid_list)