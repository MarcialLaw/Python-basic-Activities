#import csv
#from csv 
#import sys
#List_Student = ['name', 'bdate', 'sex', 'age', 'add']
#Student_List = 'List.sys'

def display_menu():
	print("---" * 20)
	print("Student Information System")
	print("---" * 20)
	print("[1] - Add new Record ")
	print("[2] - Display Record.")
	print("[3] - Search Student")
	print("[4] - Update Record")
	print("[5] - Delete Record")
	print("[6] - Exit.")
def add_student():
    print("---"*5)
    print("Add new Record")
    print("---"*5)

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
    print("Age: ", year - Age)
    print("Birthday: ", bdate)
    print("Sex: ", sex)
    print("Address: ", add)

def view_student():
    
    print("    Display Record(s)    ")
    print("    Students Record(s)   ")
    
    

while True:
	display_menu()
	
	choice = input("Enter your Choice: ")
	if choice == '1':
		add_student()
	elif choice == '2':
		view_student()
	elif choice == '3':
		search_student()
	elif choice == '4':
		update_student()
	elif choice == '5':
		delete_student()
	else:
		break
		
print("------------")
print(" Thank you! ")
print("------------")


