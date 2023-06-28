class Parent:
    def func1(self):
        print("aThis is Parent")

class Child(Parent):
    def func1(self):
        print("This is Child")

ob = Child()
ob.func1()

