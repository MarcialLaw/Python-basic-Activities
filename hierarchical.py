class Parent:
    def func1(self):
        print("This is fun")

class Child(Parent):
    def func2(self):
        print("This is fun!")

class Child2(Parent):
    def func3(self):
        print("This is fun!!")

ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()
#ob.func3()
