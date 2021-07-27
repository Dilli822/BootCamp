


def add(a,b):
     return a+b
add(5, 50) 


# iterator sin python
# iterables 
my_lists = ["monitor", "motherboard", "cpu"]
print(my_lists)

my_iterator = my_lists.__iter__()
print(my_iterator)
print(set(my_iterator))
print(tuple(my_iterator))

# classes in python
# class objec
# here we created class object vehicle and
# pass it with pass statement 
# and make an obj with v
# ariable ibj

# class vehicle:
#      pass

# def __init__(self, color, doors):
#      self.color = color
#      self.doors = doors

# vehicle("red", 5)
# print(vehicle)

class MyClass:
     x = 5
p1 = MyClass()
print(p1.x)

class MyName:
     name = "dilli"

myname = MyName()
print(myname.name)

# creating class
class Object:
     def __init__(self, name, age):
          self.name = name
          self.age = age

Object("john", 25)
print(Object)
var = Object("hari", 45)
print(var.name)
print(var.age)


class Gender:
     def hari(name, age):
          name = "hari"
          age = 45
     
Gender()
p2 = Gender()






