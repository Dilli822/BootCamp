

  # There are many python strings built in functions which can be used with strings
  >>> string = "dilli"
>>> len(string)
5
>>> string(bool)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> bool(string)
True
>>> map(string)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: map() must have at least two arguments.
>>> slice(string)
slice(None, 'dilli', None)
>>> type(string)
<class 'str'>
>>> map(string)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: map() must have at least two arguments.
>>> 

# python string methods

 >>> str1 = "mineral water"
>>> str1.capitalize()
'Mineral water'
>>> str1.lower()
'mineral water'
>>> str1.split()
['mineral', 'water']
>>> str1
'mineral water'
>>> ''.join(str1)
'mineral water'
>>> str1.replacr('best', 'water', 'is')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'replacr'
>>> str1.replace('mineral','water')
'water water'
>>> str1.title()
'Mineral Water'
>>> >>> str1.replace('mineral','water')
'water water'
>>> str1.title()
'Mineral Water'
>>> str2 = "water"
>>> str3 = "water"
>>> str1.find(str3)
8
>>> str1.find(str3)
8
>>> str1
'mineral water'
//shows the indexing position of water on str1




