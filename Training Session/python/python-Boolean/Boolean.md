
    #  Python Boolean
    #they are data types representing true and false
    they are defined by keywords true or false 
    # false =0 and true = 1 
    # can be used with arithmetic operator

   >>> x = 2
   >>> y = 3
   >>> x > y
   False
   >>> x < y
   True
   >>> x = y
   >>> x == y
   True
   >>> x = 5
   >>> y = 4
   >>> x != y
    True
   >>> x == y
   False
   >>> not(True)
   False
   >>> not(False)
   True
   >>> 

   #we can assign it with airthmetic operator
   >>> True + True
   2
  >>> True + 3
  4
   >>> false * 20
   Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
   NameError: name 'false' is not defined
   >>> False * 10
   0
   >>> True * 5
   5 
   bool() method is used to deduct either the value is truthy or falsely

   # any non-empty strings, set, dictionary, tuplen holding some value always return True in python
    >>> bool("hello I'm string")
True
>>> bool(45)
True
>>> bool(45.451)
True
>>> #list
>>> bool(['1','2','a'])
True
   >>> #tuple
   >>> bool((1,2,3))
    True
   #dictionary
   >>> bool({1,2,3})
   True
    
    #Empty list,set,dictionary,tuple ,none value always return false

   >>> bool(False)
   False
   >>> bool(None)
   False
   >>> bool(0)
   False
   >>> bool("")
   False
   >>> bool(())
   False
   >>> bool([])
   False
   >>> bool({})
   False

   #checking with conditional statements in python
   >>> >>> a = 'abc'
   >>> if a:
   ...    print(a)
    ... else:
    ...     print('this is empty')
    ... 
       abc
       
    >>> b = ''
     >>> if b:
      ...   print("not empty")
       ... else:
        ...    print("this is empty")
        ... 
       this is empty

      



    