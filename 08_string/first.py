# # strings in python
# chai="masala chai"
# print(chai)
# print(chai[0])


# # slicing 

# slice_chai=chai[0:6]
# print(slice_chai)
# print(chai[-1])#will print first element from end
# print(chai[:])#will print whole string bcoz sliced whole string
# num_list="0123456789"
# print(num_list[0:7:2])#third param for hop
# print(num_list[0:15])#will print till last element if slicing out of bound
# print(num_list[11:15])#nothing will be printed


#string methods

# chai="ginger chai"
# print(chai)
# print(chai.upper())
# chai1="  lemon        chai     "
# print(chai1.strip())#removes extra spaces in begining and end
# print(chai.replace("ginger", "black"))#replacing ginger with black


# chai1="ginger, masala, lemon, mint, chai, chai"
# print(chai1)
# print(type(chai1))
# chai1_split = chai1.split(", ") #converting cha1 string into list
# print(chai1_split)
# print(type(chai1_split))

# print(chai1.find("masala"))#will return index of first elemenet if found
# print(chai1.count("chai"))#will print no occurances



#order formatting in string

# chai_type="masala"
# quan= 2
# order = "I want {} cup of {} chai"
# print(order.format(quan, chai_type))
# chai1=["ginger", "masala", "lemon", "mint", "chai", "chai"]
# new_chai = "-".join(chai1) #converting list into string elements seperated by -
# # print(new_chai)
# # print(len(new_chai))

# for letter in new_chai:
#     print(letter)


#####################
#"he said, "masala chai is awesome."" printing string like this--

# str1="he said, \"masala chai is awesome.\""
# print(str1)
# str2= "masala\nchai" ## here \n willl work for adding new line but if we want to print as it is...
# str3=r"masala\nchai"#after r all are raw string
# print(str2)
# print(str3)

# path="c:\\user\\pwd\\py" #printing a directory
# print(path)
# path1=r"c:\\user\\pwd\\py"  # r- means raw
# print(path1)



chai="masala ginger lemon mint"
print("masala" in chai) #will tell is masala present in chai or not
 






