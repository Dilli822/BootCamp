
  # String Format Method
  # it is handled by calling .format() on a string object
  # 
  >>> 'I am {age} years old'.format(age=22)
'I am 22 years old'
>>> 'I am {}'.format('Dilli Hang Rai')
'I am Dilli Hang Rai'

 # for larger number of format() method = positional arguments
 # positional arguments are inserted into the template in place of nubered replacement fields
 # example
 'I am {0} and I am {1} years old'.format('dilli',19)
'I am dilli and I am 19 years old'

'I have {1}, {0}, and {2} in my bag.'.format('book', 'pen', 'copy')'I have pen, book, and copy in my bag.'

 # before the python3 we used to do the indexing to positional arguments 
 # but after python3 no need to do this because python assume them in sequential order(automatic field numbering)
 'I am {} and I am {} kg.'.format('dilli hang', 58.58)
'I am dilli hang and I am 58.58 kg.'

# errors
   'I am learning {1},{0},{2} and {3} now.'format('javascript', 'python , 'nodejs','django')
IndentationError: unexpected indent
>>> 'I have {1}, {0}, and {2} in my bag.'.format('book', 'pen', 'copy)
  File "<stdin>", line 1
    'I have {1}, {0}, and {2} in my bag.'.format('book', 'pen', 'copy)
                                                                      ^
SyntaxError: EOL while scanning string literal
>>> 'I have {1}, {0}, and {2} in my bag.'.format('book', 'pen', 'copy')'I have pen, book, and copy in my bag.'
>>> 