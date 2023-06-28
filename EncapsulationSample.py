class Encapsulation:
    def __init__(self):
        self.publicAttribute = 1
        self._protectedAttribute = 2
        self.__privateAttribute = 3

    def publicMethod(self):
        print("Text from publicMethod method")

    def _protectedMethod(self):
        print("text frmo protectedMethod method")

    def __privateMethod(self):
        print("Text from privateMethod method")

obj = Encapsulation()
print(obj.publicAttribute)
print(obj._protectedAttribute)
#print(obj.__privateAttribute)

obj.publicMethod()
obj._protectedMethod()
#obj.__privateAttribute
