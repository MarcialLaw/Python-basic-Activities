#PROGRAM THAT TAKE THE COMPLETE NAME
#AND BIRTHDAY OF A PERSON

name = input("Complete Name: ")

Len = len(name)

Comma1_index = name.index(",")
Fname = name[0:Comma1_index]
MI_index = (Comma1_index + 2)
MI = name[MI_index] + "."
Comma2_index = name[MI_index+1:Len].index(",")
Lname = name[Comma2_index+MI_index+3:Len]

print(Fname, MI, Lname)

sex = input("Sex: ")
Birthdate = input("Birthdate: ")

strBDAY = len(Birthdate)
Comma_index = Birthdate.index(",")
Age = int(Birthdate[Comma_index+5: strBDAY])

import datetime

today = (datetime.datetime.now().year)

if (sex.upper() == "MALE"):
              print("Hello Mr." , Fname, MI, Lname)

else:
              print("Hello Ms." , Fname, MI, Lname)

print("Your age now is ", today-Age)
