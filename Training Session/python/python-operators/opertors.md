

  #sign/symbols to do task like airthmetic operators
  #addition,subtraction,division,multiplication
  #modules %

  #comparison operators
  !=
  ==

  #logical operators


  #identity operators

  # == checks only value of variables whereas
  # is and is not check whether the obj is same or not

  a = 1
  b = 1
  id(a)
  id(b)
  a == b
  both id will be same because both are same obj
  a is b
  true 

  a = []
  b = []
  id(a)
  id(b)
  but both are different obj
  with different ids
  but both are empty or null variables 
  so c == d
  true


#membership operators
in or in not
>>> z = [1,2,3]
>>> 1 in z
True
>>> 5 in z
False
>>> 2 in z
True

#dicitonary
Dictionary in Python is an ordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.

>>> d = {'a': 1, 'b':2, 'c':3}
>>> 'a' in d
False
>>> 'f' in d
false
>>> 'a' in d
True

#bitwise operator 
used for binary comparison

a = 0011 1100
b = 0000 1101
AND:a&b = 0000 1100

OR:a|b = 0011 1101

XOR: a^b = 0011 0001

NOT: ~a = 1100 0011

this a & b will do and operation ,  a|b will do OR operation, a^b will do XOR Operation, ~a will do not operation

this is fast operator and rarely used in python
but hugely used in low level progamming


#Left & Right shift bitwise operators
#Left Shift
>>> x = 3
binary value is 0011
shifted left by pushing 2 zeroes in from the right that makes it 1100 which is 12 
>>> x << 2
12

#Right shift
x = 12
binnary value is 1100
x >> 2
x = 3
#just reverse concepts/process of left shift
>>> x = 12
>>> x >> 2
3

#Assignments Operators
arithemetic + isequql to 
+=
**=

#operators precedence
if two or more than operators comes together then the priority comes like
[]properties is top most pririoty
where OR | is lower most priorioty

#Associativity in python
if all the priority comes together then,
expression having multiple operators of same precedence 
#commonly found
#left-right associativity
print(3 *4 //5)
print 2

#for double exponentional it will be right to left
#right-left-associativity
>>> print(2 **3 **2)
first 3 ^ 2 = 9
then 2 ^ 9 
is 512
512
>>> 





