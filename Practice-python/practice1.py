class Books:
   def __init__(self, name, price):
    self.name = name
    self.price = price

book = Books("maths", 950)
print(book.name)
print(book.price)


# using lambda
add = lambda a,b: a + b
r = add(2, 5)
print(r)


mul = lambda x,y: x * y
n = mul(5, 5)
print(n)

div = lambda x,y: x % y
d = div(50,2)
print(d)


# using lambda
a = lambda x,y: x + y
b = a(45, 45)
print(b)

