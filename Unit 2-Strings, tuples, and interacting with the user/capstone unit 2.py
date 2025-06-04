#The problem
#This is your first interactive programming task, so let's have some fun with the user! You want to write a program that automatically combines two names given by the user. 
# That's an open-ended problem statement, so let's add a few more details and restrictions:
#Tell the user to give you two names in the format: FIRST LAST
#Show the user two possible new names in the format:FIRST LAST.
#The new first name is a combination of the first names given by the user, and the new last name is a combination of the last names given by the user. 
#For example, if the user gives you Alice Cat and Bob, a possible mashup is Bolice Dot.

user_first=input("Give two names: ") #ask the user to give two names
answer_1=user_first.upper() #make the answer uppercase
print(answer_1)


user_second=input("Give again two names: ") #ask the user to give two names
answer_2=user_second.upper() #make the answer uppercase
print(answer_2)

split_names_1=answer_1.split()
split_names_2=answer_2.split()
print(split_names_1)
print(type(split_names_2))

