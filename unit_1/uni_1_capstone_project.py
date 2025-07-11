# The problem
# the first programming task you'll see is to write a program in Python that, converts minutes to hours.
# Your program will take that number, do some calculations and print out the conversion to hours and minutes. 
#Your program should print the result in the following way. If the number of minutes is 121, the program should print this: Hours 2 Minutes 1.

minutes=35
minutes_to_convert=minutes/60 #here I get a float number which doesn't correspond to hours
print(minutes_to_convert) 

hours_rounded=int(minutes_to_convert) #here I add round instead of int, it worked for numbers >60 but not numbers<60. After trying a few times by myself, i picked quickly at the solution and changed to int. Now it works no matter the number.
print(hours_rounded)

minute_try=minutes_to_convert-hours_rounded #I had an int here, but I removed it when I added int to hours_rounded. It was no longer necessary.
print(minute_try)

minutes=round(minute_try*60)

print("Hours",hours_rounded,"Minutes",minutes)

