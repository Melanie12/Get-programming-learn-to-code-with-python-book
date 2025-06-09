# Capstone Unit 3

#The problem
# You'll use conditionals and branching to create a story. At each scene, the user will enter a word.
# The word will tell the program which path to continue following.
# Your program should handle all possible paths that the user might choose, but doesn't need to handle any unexpected input from the user.

print("You are in a deserted island in a 2D world")
print("Try to survive until rescues arrives!")
print("Any other command exits the program")

user_input=input("choose a direction: ")
answer_1=user_input.upper()
print(answer_1)

if answer_1=="LEFT":
    input_2=input("You are in front of a pyramid would you like to climb it? YES/NO ")
    answer_2=input_2.upper()
    print(answer_2)
    if answer_2=="YES":
        print(answer_2)
        print("you can signal to the helicopter rescue")
    elif  answer_2=="NO":
        print("You will starve to death")
elif answer_1=="RIGHT":
    input_3=input("Do you see a boat? YES/NO ")
    answer_3=input_3.upper()
    print(answer_3)
    if answer_3=="NO":
        print("Find wood and make a boat")
    elif answer_3=="YES":
        print("Take the boat and leave the island")
else:
    print("You can only type left or right")
    print("Pick a direction")
