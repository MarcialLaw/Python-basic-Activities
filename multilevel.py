class Parent:
    def func1(self):
        print("This is fun")

class Child(Parent):
    def func2(self):
        print("This is funny")

class Child1(Child):
    def func3(self):
        print("This is it")

ob = Child1()
ob.func1()
ob.func2()
ob.func3()
