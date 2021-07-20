
 # python doesnot allow to delete the string once it is assigned because they are immutable but we can reassign different string to the same name
 # but we can delete the whole string at once with del keyword

 >>> message = "hello world from python"
>>> message [5] = 'W'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

>> #removing character of string
>>> message = "hey everyone"
>>> del message[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object doesn't support item deletion
>>> 

>>> #removing string but we can remove or delete the whole string at once
>>> message = "i am being deleted by python del keyword"
>>> del message
>>> #deleted successfullt
>>> message
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'message' is not defined
>>> 