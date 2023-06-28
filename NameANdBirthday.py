#PROGRAM THAT TAKE THE COMPLETE NAME
#AND BIRTHDAY OF A PERSON

strname = input("Complete Name: ")

intStrLen = len(strname)
intComma1_index = strname.index(",")
strFname = strname[0:intComma1_index]
intMI_index = (intComma1_index + 2)
strMI = strname[intMI_index] + "."
intComma2_index = strname[intMI_index+1:intStrLen].index(",")
strLname = strname[intComma2_index+intMI_index+3:intStrLen]

print(strFname, strMI, strLname)

strsex = input("Sex: ")
strBirthdate = input("Birthdate: ")

if (strsex.upper() == "MALE"):
              print("Hello Mr." , strname)

else:
              print("Hello Ms." , strname)

