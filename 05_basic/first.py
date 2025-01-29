# # python datatypes (also called as datatype object)

# # python supports high precision for floats
# print(3*2.77)

# # supports bigger multipication like--
# print(2**1000)
# print("\n")
# print(54523562645734*3333333333333789)

# importing libraries
# import math
# import random

# print(math.pi)

# print(random.random() )##for rinting random values

# print(random.choice([1,2,3,4,5])) #will give random value from this array

#strings

# username="chaiaurcode"
# print(len(username)) #len() method for finding the length of a string

# print(username[0])
# # username[0]="a" # we cant do assignment in string bcoz strings  are immutable(error)

# # negative index will give value at position from end..

# print(username[-1])
# print(username[1:5]) #prints string from 1 index to 4 index , last index is not included

# print(dir(username))#will give list operation we can perform on string



# #In python arrays are treated as list

# myList = [123,'A',"string",4.5]
# print(myList)
# print(len(myList))
# print(myList[1])

# #Dictionaries (stores values as key value pairs)

# myDict = {'one':"giner chai", 'two':"lemon chai",'three':"masala chai"}
# print(myDict)
# print(myDict['one'])
# print(myDict['four']) #will give error 'four' key is not present


#Tuples-

myTup = (1,2,3,4,5)
print(myTup)
print(myTup[1])
print(myTup[-1])
print(len(myTup))

