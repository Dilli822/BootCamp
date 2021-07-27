


my_lists = ["apple","linux","samsung","acer"]
my_lists.pop()
print(my_lists)

n = my_lists.__iter__()
print(n)

print(n.__next__())

print(n.__next__())

print(n.__next__())

# now error will occur
# stopIteration

for i in n:
    print(i)


def func():
    val = 8
    print("this is local variable running from local environment", val)

func()

val = 48
func()
print("this is global variables running on global environment", val)

# now making the func body local var to global var by overwriting the valriables

def func():
     val = 40
     print("this is overwrite global val", val)

func()


# iterators
this_is_iterables = ["yes","i","am", "iterables"]
print(this_is_iterables)
type(this_is_iterables)

# now we find it is iterables or not
print(dir(this_is_iterables))

# now making it to iterators

making_it_iterators = this_is_iterables.__iter__()
print(making_it_iterators)

# as we know iterator supports next
print(making_it_iterators.__next__())

# applying loop
for i in making_it_iterators:
    print(i)


