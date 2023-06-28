class Parent:
    def func1(self):
        print("This is function 1")
class Child():
    def func2(self):
        print("This is function 2")
class Child1(Child):
    def func3(self):
        print("This is function 3")

class Child2(Child1):
    def func4(self):
        print("This is function 4")

class Child3(Parent,Child):
    def func5(self):
        print(".....")

    #def func1(self):
        #print("This is function 1 of child 3")

ob=Child3()
ob.func1()
ob.func2()
#ob=Child2()
ob.func5()
