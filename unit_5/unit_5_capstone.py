# Analyze your friends

# The problem
# Write a program that reads input from a file in a specific format, regarding all your friends' names and phone numbers. Your program should store that information and analyze it in some way.
# For example, you can show the user where their friends live based on the area code of the phone numbers, and the number of states where they live.

def read_file(file):
    """
    file, a file object
    starting from the first line, it reads every 2 lines and stores them in a tuple
    Starting from the second line, it reads every 2 lines and stores them in a tuple.
    Returns a tuple of the two tuples.
    """
    first_every_2=() #empty tuples for names
    second_every_2=() #empty tuples for phone numbers
    line_count=0 #counter for line number
    for line in file: #loops through every line
        stripped_line=line.replace("\n","") #removes newline character
        if line_count%2 ==0: #odd-numbered lines
            first_every_2 +=(stripped_line,) #add to the names tuple
        elif line_count%2 ==1: #even-numbered lines
            second_every_2+=(stripped_line,) #adds to the phone tuple
        line_count+=1 #increments line number
    return (first_every_2,second_every_2) #returns a tuple of tuples

def sanitize(some_tuple):
    """
    phones, a tuple of strings
    removes all spaces, dashes, and open/closed parentheses in each string
    returns a tuple with cleaned up string elements
    """
    clean_string=() #replaces unnecessary characters with empty string
    for st in some_tuple:
        st=st.replace(" ","")
        st=st.replace("-","")
        st=st.replace("(","")
        st=st.replace(")","")
        clean_string +=(st,) #adds cleaned number to new tuple
    return clean_string #returns new tuple


friends_file=open('friends.txt') #opens the file
(names,phones)=read_file(friends_file) #calls function

print(names)
print(phones)
clean_phones=sanitize(phones) #sees whether your function worked

print(clean_phones) #outputs printed to the user
friends_file.close() #closes the file

map_file=open('map_area_codes_states.txt')
(areacodes,places)=read_file(map_file)

def analyze_friends(names,phones,all_areacodes,all_places):
    """
    names, a tuple of friend names
    phones, a tuple of phone numbers without special symbols
    all_areacodes, a tuple of strings for the area codes
    all_places, a tuple of strings for the US states
    Prints out how many friends you have and every unique
    state that is represented by their phone numbers
    """

    def get_unique_area_codes():
        """
        Returns a tuple of all unique area codes in phones
        """
        area_codes=() #tuple to contain unique area codes
        for ph in phones: #goes through every area code, variable phones is a parameter to analyze_friends
            if ph[0:3] not in area_codes: #checks that area code isn't there
                area_codes += (ph[0:3],) #concatenates tuple of unique codes with a singleton tuple
        return area_codes

    def get_states(some_areacodes):
        """
        some_areacodes, a tuple of area codes
        returns a tuple of the states associated with those area codes
        """        
        states =()
        for ac in some_areacodes:
            if ac not in all_areacodes:
                states +=("BAD AREACODE",)
            else:
                index=all_areacodes.index(ac)
                states += (all_places[index],)
        return states

    num_friends=len(names)
    unique_area_codes=get_unique_area_codes()
    unique_states=get_states(unique_area_codes)
    print("You have", num_friends,"friends!")
    print("They live in", unique_states)

friends_file=open('friends.txt')
(names, phones)=read_file(friends_file)
areacodes_file=open('map_areacodes_states.txt')
(areacodes,states)=read_file(areacodes_file)

clean_phones=sanitize(phones)
analyze_friends(names,clean_phones,areacodes,states)

friends_file.close()
areacodes_file.close()