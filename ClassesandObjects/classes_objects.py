class MyClass:
    def myfunc(self):
        pass

    def display(self, name):
        print("Name is", name)
    def m1(self):
        print("instance method  ")

    def m2(self):
        print("Static method ")

mc = MyClass()
mc.myfunc()
mc.display('Scott')
mc.m1()
MyClass.m2(10)
