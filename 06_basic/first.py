# import sys

# #ref_count is internally maintained by python for memory location (that how many variables refernce to that memory location)
# print(sys.getrefcount("sjkdf"))
# print(sys.getrefcount(5))
# print(sys.getrefcount("sjkdsdff"))
# print(sys.getrefcount(7835))
# username = "VSC"
# print(sys.getrefcount(username))# we can not know exact ref count , this method give ref count for the values and string which are not strored in memory

# # in python variable does not have to do anything with data type like in c++, it reference to memory location where a particalar type of data is stored , same variable can reference to other type of data also but not possible in language like c++ 
# # python doesnot assign datatype to variable but data in memory has datatype, that datatype assigned in memory


# a = 123
# print(a)
# a = "string" #now val 123 has no reference so garbage collector will clean immediately , happens exactly same but not in case of string and number bcoz string and numbers are used a lot in program so python do optimization by not immediatly cleaning empty referenced num or string bcoz those can be used in near future 
# # garabage collection of num and string happpens late 
# print(a)

####################################################
m=[1,2,3,4]
n=m
# print(m==n)#true
# print(m is n)#true
m=[1,2,3,4]
print(m==n)#true , this check for content
print(m is n)#false bcoz this checks for reference 

# but not same in case of string as above
a="str"
b=a
print(a is b)#true
print(a==b)#true
b="1"
b="str"
print(a is b)#true
print(a==b)#true



