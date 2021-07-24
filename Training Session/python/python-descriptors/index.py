

class MyClass:
     def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 100

        def setter(self, value) -> None:
            print("accessing the attribute to set the value")
            raise AttributeError("Cannot change the value")

        attr1 = property(getter, setter)
        
     obj = MyClass()
     x = obj.attr1
     print(x)