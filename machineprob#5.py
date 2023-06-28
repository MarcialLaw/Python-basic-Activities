class IOString():
    def __init__(self):
        self.str1 =""

    def get__String(self):
        self.str1 = input()

    def print__String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get__String()
str1.print__String()
