print ("         Student Infromation System!         ")
print ("         ___________________________\n       ")
print ("         [1] - Add New Record                ")
print ("         [2] - Display Record                ")
print ("         [3] - Update Record                 ")
print ("         [4] - Delete Record                 ")
print ("         [5] - Exit                          ")
print ("         ___________________________         ")

import statistics
record = []

Op = input("    Enter Your Choice:___    ")
print("==================================================")
def new_student():
    if len(record) > 20:
        print("Student data exceeded!")
        return
        import datetime
        year = (datetime.datetime.now().year)
        month = (datetime.datetime.now().month)
        day = (datetime.datetime.now().day)
        print("1. Add New Record)""  ""Current Date:",month,-day,-year)
        print("Enter the student data")
        data = []
        Fname = input("First Name:_____")
        Mname = input("Middle Name:____")
        Lname = input("Last Name:____")
        bdate = input("Birthdate:____")
        sex = input("Sex:____")
        add = input("Address:____")

        print("      New student's record sucessfully saved!      ")
        print("===================================================")

        bd = len(bdate)
        intComma2_Index = bdate.index(',')
        Age = int(bdate[intComma2_Index+5:bd])
        if (sex.upper() == "MALE"):
                        print(" Name: Mr.", Lname, Fname, Mname)

        else:
            print("Name: Ms.", Lname, Fname, Mname)
        data.append(Fname)
        data.append(Mname)
        data.append(Lname)
        data.append(bdate)
        data.append(sex)
        data.append(add)
        return
num = input("   Another Transaction?:    \n")
print(" ")
if (num.upper()=="YES"):
        Fnam1 = input("First name: ")
        Mname1 = input("Middle name: ")
        Lname1 = input("Last name: ")
        bdate1 = input("Birthdate: ")
        sex1 = input("Sex: ")
        add1 = input("Address: ")

        print("      New student's record sucessfully saved!      ")
        print("===================================================")
        bc = len(bdate1)
        intComma2_Index = bdate1.index(',')
        Age = int(bdate1[intComma2_Index+5:bc])
        if (sex1.upper() == "MALE"):
            print(" Name: Mr.", Lname1,',', Fnam1,',', Mname1)

        else:
            print("Name: Ms.", Lname1, ',', Fnam1, ',', Mname1)
        print("Age:", year  - Age, "years old")
        print("Birthday:", bdate1)
        print("Sex:", sex1)
        print("Address:", add1)
            
Op = input("    Enter Your Choice:___    ")
if Op == '2':
    print("    Display Record(s)    ")
    print("    Students Record(s)   ")
    if (sex.upper() == "MALE"):
        print(" Name: Mr.", Lname, ',', Fname, ',', Mname)

    else:
        print("Name: Ms.", Lname, ',', Fname, ',', Mname)
    print("Age:", year  - Age, "years old")
    print("Birthday:", bdate)
    print("Sex:", sex)
    print("Address:", add)

    if (sex.upper() == "MALE"):
                 print(" Name: Mr.", Lname1, ',', Fnam1, ',', Mname1)

    else:
        print("Name: Ms.", Lname1, ',', Fnam1, ',', Mname1)
    print("Age:", year  - Age, "years old")
    print("Birthday:", bdate1)
    print("Sex:", sex1)
    print("Address:", add1)


if Op == '3':
        print("Unable to Update!")


if Op == '4':
        print("Warning! Records will be deleted!")

if Op == '5':
        print("Exit")

else:
    print("Invalid Syntax!")



    
