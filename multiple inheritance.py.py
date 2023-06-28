class Base1(object):
    def __init__(self):
        self.str1 = "BASE1"
        print ("TRY")

class Base2(object):
    def __init__(self):
        self.str2 = "BASE2"
        print ("HELLO")


class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print ("HIGH")

    def printStrs(self):
        print(self.str2, self.str1)

        
ob = Derived()
ob.printStrs()
obj = Base2()
obj.__init__()

