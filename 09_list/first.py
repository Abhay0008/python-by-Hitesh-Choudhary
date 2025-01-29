# list in python
chai_variety=["black","green","oolong","white"]
# print(chai_variety)
# print(chai_variety[0])
# #methods like slicing and other are also present in list like string

# print(chai_variety[-1])
# print(chai_variety[1:3])#slicing

# print(chai_variety[1:2])

# chai_variety[1:2]="tulsi" #this will place "tulsi" at index 1 but will treat "tulsi" as a string not a list 
# print(chai_variety)

# chai_variety[1:2]=["tulsi"]
# print(chai_variety)#now "tulsi will  be treated as a single element of list"
# print(chai_variety[2:6])

# chai_variety[2:6]=["adrak"]#replacing multiple element with single element
# print(chai_variety)

# print(chai_variety[4:4])#will not give anything (will give empty list ) bcoz last index is excluded
# chai_variety[1:1]=["tst","test"]
# print(chai_variety)

# chai_variety[1:3]=[]# insert nothing work similar to deletion opoeration
# print(chai_variety)

##looping on list
# for chai in chai_variety:
#     print(chai)
# print bydefault end with new line is we dont want to print element in new line in each iteration , we can do following


# for chai in chai_variety:
#     print(chai, end=", ")
# chai_variety.append("new chai")
# # for chai in chai_variety:
# #     print(chai, end=", ")

# chai_variety.remove("new chai") #for removing an element(given element)
# for chai in chai_variety:
#     print(chai, end=", ")
# print("\n")
# print(chai_variety.pop())#removes an element from end
# for chai in chai_variety:
#     print(chai, end=", ")

##inserting an element in list
# chai_variety.insert(0,"MMM chai")

# for chai in chai_variety:
#     print(chai, end=", ")


# #if we do chai_copy=chai_variety then memory location will be same for both and both reference to same memory location

# chai_copy=chai_variety.copy() #now new memory location is created for chai_copy and both var reference to diff diff memory location
# print("\n",chai_copy)



## List comprehension

print(range(10))
square_num=[x**2 for x in range(5)]# in range last one is always excluded , same in case of slicing
print(square_num)
cube_num=[x**3 for x in range(5)]
print(cube_num)