# class notes


# Immutable(Unchangeable) and mutable(changeable) in python
# In Python, mutable data types are data types that can be changed after they are created
# mutable-- Lists, Dictionaries, Sets, User-Defined Classes, Array
# immutable-- Numbers (Integer, Float, Complex, Decimal, Rational & Booleans), Tuples, Strings, Frozen Sets, Bytes

# Almost everything in python is object (as said) , like string , array are object

# >>> username ="chaiaurcode"
# >>> username
# 'chaiaurcode'
# >>> username="chaiaurcoffe"
# >>> username
# 'chaiaurcoffe'

# confusion strings are immutable but here we can change then what immutable means? 
# for this need to understand internal working of python
# in python string and other data types are treated as object , when they get alloca\ted memory block then variable (username) point to the reference of chaiaurcode and 
# and this memory reference can not be changed this is what immutable means 
# now when chaiaurcoffe string get memory allocation then username variable points to its memory reference , and automatic garbage collector in python delete the string chaiaurcode when nothing reference to its memory

# we can not change memory refernce of chaiaurcoffe but can put another things in variable username exactly that happened in  above lines of code where get confuised

# same happen -- below
x=10 #x refernce to 10
y=x #y reference to 10
x=15 # now x reference to memory where 15 is stored but y refernce to 10 (x=15,y=10)


