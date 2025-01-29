# printing some thing on terminal
print("hello python")
print(4+5)

# function de definition with print statement
def sum(a,b):
    print(a+b)

sum(7,7)
# function definition with  return type

def mul(a,b):
    return a*b

print(mul(9,9))

chai_one="ginger chai"
chai_two="lemon chai"

# class notes(below code executed on shell)

# import os
# os.getcwd()
# 'A:\\a1\\cs\\Python\\01_basics'
# for i in "chai":
# ...     print(i)
# ...
# c
# h
# a
# i

# import sys
# sys.platform
# 'win32'

# import sum from first
  

# from first import mul
# hello python
# 9
# 14
# 81
# print(mul(9,9))
# 81

# # we can access all methods of a file using .(dot) afte
# #er importing the file


# first.sum(15,15)

 ###########After importing a file if make any changes or add some new methods in file then those changes will not reflect , NOw we either can import again that file or reload the file using reload library

# import first
# >>> first.sum(15,15)
# 30
# >>> first.chai_one

#     first.chai_one
# AttributeError: module 'first' has no attribute 'chai_one'

# >>> from importlib import reload
# >>> reload(first)
# hello python
# 9
# 14
# 81
# <module 'first' from 'A:\\a1\\cs\\Python\\01_basics\\first.py'>
# >>> first.chai_one
# 'ginger chai'
# >>> first.chai_two
# 'lemon chai'


