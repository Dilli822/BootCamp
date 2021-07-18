  
  # python string formatters
  # ways to format a string 
  1. % formating = interpolation operator
  2. format()
  3. 

  # % formatting with modulo = interpolation operatos
  # % is followed by the data type that needs to be converted or formatted
  # % operation then substitutes the %data type phrase with zero or more elements of the specified data type

  # %d is for integer
  # %s is for string
  # %f is for float
  # %.2f is for float with 2-digit floating point
  # %.4f float with 4-digit floating point
>>> 'I am currently learning %s and my skill level is %f'%('python',0.99)
'I am currently learning python and my skill level is 0.990000'

>>> 'I am currently learning %s and my skill level is %f.2f'%('python', '0.99')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be real number, not str
>>> 'I am currently learning %s and my skill level is %f.2F'%('python', '0.99')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be real number, not str

>>> 'Hi I am %s and my weight is %.2F'%('Dilli', 58.5626145)
'Hi I am Dilli and my weight is 58.56'
>>> 