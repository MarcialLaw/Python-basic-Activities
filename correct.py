strName= input("Enter your Complete Name: ")
strSex= input("Enter your Sex: ")
strBirthday= input("Enter your Birthdate: ")

intStrLen = len(strName)
intComma1_Index = strName.index(",")
strFName = strName[0:intComma1_Index]
intMI_Index = (intComma1_Index + 2)
strMI = strName[intMI_Index]+"."
intComma2_Index = strName[intMI_Index+1:intStrLen].index(",")
strLName=strName[intComma2_Index+intMI_Index+3:intStrLen]

print (strFName)
print (strMI)
print (strLName)

name = input ("Enter your name: ")
sex= input("Enter your sex: ")

if (sex.lower() == "male"):
    title = "Mr."

else:
    title = "Ms."

print("Hello "+ title + " " +name)

from datetime import date


print (date.today)


