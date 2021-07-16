
   # strings
   # sequenece of characters with valid enclosed quotes
   # starting and ending quotation same "hello world"
   # unlimited characters can be used on the strings depending upon the os system architecture
   # string must be written in a correct quotation 
   # or with alernate quote characters 
   # or with escape character '\' blackslash
    
     >>> #example of invalid string literal definition
>>> str1 = 'this is a invalid quote (') in string '
  File "<stdin>", line 1
    str1 = 'this is a invalid quote (') in string '
                                      ^
SyntaxError: invalid syntax
>>> str2 = " invalid use of alternate quote (") in a string"
  File "<stdin>", line 1
    str2 = " invalid use of alternate quote (") in a string"
                                              ^
SyntaxError: invalid syntax
>>> #example of correct alternate quote characters 
>>> str1 = "single quote as alternate quote (') in string"
>>> print(str1)
single quote as alternate quote (') in string
>>> str2 = 'Double quote as an alternate quote(") in a string'
>>> print(str2)
Double quote as an alternate quote(") in a string
>>> # correct example of escape character '\'
>>> str1 = ' using single escape character (
  File "<stdin>", line 1
    str1 = ' using single escape character (
                                           ^
SyntaxError: EOL while scanning string literal
>>> str1 = 'usign single alternate quote (\') in a string'
>>> printstr1)
  File "<stdin>", line 1
    printstr1)
             ^
SyntaxError: invalid syntax
>>> print(str1)
usign single alternate quote (') in a string
>>> str2 = " using double alternate quote string(\") in a string "
>>> print(str2)
 using double alternate quote string(") in a string 
>>> 

   # why alternate quotes ?

   In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return. ...
  
  # if we just use the string with enclosed single quote then it is simply a string
   for eg: str1 = 'Hey I am dilli'
   # if we add another single quote inside the str1
   str1 = 'Hi I'm dilli'
    File "<stdin>", line 1
    str2 = 'Hi I'm Dilli'
                 ^
   SyntaxError: invalid syntax
   # this happens because python understands that hi i' is complete string with single enclosed string
   
   # so to prevent this we need to add alternate quote to make sure that python continue to read the characters and also backslash as string characters
   #  with backslash we have
    str2 = 'Hi I\'m dilli'
    >>> print(str2)
    Hi I'm dilli //output

    # suppressing special character meaning
    >>> print('a\
   ... b\
   ... c\
   ... d\
   ... e')
   abcde
    
    >>> print('x\
    ... y\
    ... z')
    xyz

    # From above both examples we see that python terminates/ignore the new line and read the backslask(\) as character inside a single quote

    print('x\\y')
    x\y
    # here  python ignore one backslash and takes another backslash as character

    # Raw strings
    if strings are raw then it takes the escape sequences as normal characters
    # we can just add r or R to make the string raw
    # none raw strings or not using r 

    >>> # example
    >>> print('hello\nworld')
    hello
    world
    # here \n  starts a new line
    
    print('hello\\world')
    hello\world

    #raw strings example or using r 
    >>> print(r'hello\nworld')
    hello\nworld
    >>> print(R'hello\\world')
    hello\\world

    #Here R and r has ignored the escape sequences as  python treated them all as characters
    




   
    