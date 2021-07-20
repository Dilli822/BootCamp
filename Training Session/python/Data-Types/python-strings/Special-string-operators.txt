

   # if variable a holds 'hello' and b holds 'world' then:
   >>> a = "hello"
>>> b ="world"
>>> a + b
'helloworld'
>>> a*2
'hellohello'
>>> b*2
'worldworld'
>>> a[0]
'h'
>>> b[0]
'w'
>>> a[0:1]
'h'
>>> e in a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'e' is not defined
>>> 'e' in a
True
>>> 'w; in b
  File "<stdin>", line 1
    'w; in b
            ^
SyntaxError: EOL while scanning string literal
>>> 'w' in b
True
>>> 'z' in a
False
>>> 'f' not in a
True
>>> 'h' not in a
False
>>> 