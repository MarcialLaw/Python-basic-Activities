class Student:
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2


    def accept(self, Name, Rollno, Marks1, Marks2):
        ob = Student(Name, Rollno, Marks1, Marks2)
        ls.append(ob)

    def display(ob):
        print("Name : ", ob.Name)
        print("Roll No : ", ob.Rollno)
        print("Marks1 : ", ob.Marks1)
        print("Mraks2: ", ob.Marks2)
        prirnt("\n")

    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i

    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]

    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll;

ls =[]
obj = Student('',0, 0, 0)

print("\n")
print("\n1.Accept Student Details\n2.Display Student Record" /
       "\n3.Search Stuent Record\n4.Delete Record" /
       "\n5.Update Record\n6.Exit")

obj.accept("A", 1, 100, 100)
obj.accept("A", 1, 100, 100)
obj.accept("A", 1, 100, 100)

print("\n")
print("Student List!")
for i in range(ls.__len__()):
      obj.display(ls[i])
print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])


