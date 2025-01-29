# numbers in python

#libraries like numpy gives the advantage in python to perform all the operations in python which requires matlab
# number in python is not merey an object but it is a group of object
# boolean is also treated as number
# avoid evaluation of mathematical expression on the basis of precision like-- x+y*z
# but in real word production enclose with paranthesis to which needs to evaluate first
# (x+y)*z or x+(y*z)
# dont work like-- 2+3.3
# always specify the type-- 
# print(2+int(4.5)) 
# print(float(2)+4.5)

# # operator overloading-- operator itself decides what operation to do--
# print("wel"+"come")#with string -- concatenate
# print(5+5)#with number -- addition
# x=2
# y=5
# z=7
# print((x,y,z))
# # python can handle large numbers like pow(2,1000)
# print(2**10000)

# comparison-- ==, <,>,<=,>=,!=

# print(3>5)
# print(2<3)

# import math

# print(math.floor(3.7))
# print(math.floor(-3.7))
# print(math.ceil(3.7))
# print(math.ceil(-3.7))
# print(math.trunc(2.8))
# print(math.trunc(-2.8))

# print(0o20) #tells whats octal value is 20
# print(0xff)
# print(0b1000)
# print(hex(64)) #tells hex value of 64
# print(bin(6))

# print(int("6",8)) #converting int 8(base 10) into value of base 8

# print(int('20',16))


# import random

# print(random.randint(1,10)) #will print random integer from 1 to 10
# print(random.randint(1,10))
# print(random.randint(1,10))
# print(random.randint(1,10))
# print(random.randint(1,10))
# l1=["masala chai","ginger chai","lemon chai"]
# print(random.choice(l1))
# random.shuffle(l1)
# print(l1)



###############################

# print(0.1+0.1+0.1)
# print((0.1+0.1+0.1)-0.3) #output will be- 5.551115123125783e-17
# #to avoid this

# from decimal import Decimal
# print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1'))
# print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))


# from fractions import Fraction

# myfra=Fraction(2,3)
# print(myfra)


######sets

# set1={1,2,3,4,5}
# print(set1)
# print(set1 & {1,2})#will give intersection
# print(set1 & {7,8})
# print(set1 | {9,0}) # will give union
# print(set1-{1,2}) #will give difference



############
print(type(True))
print(1==True)
print(0==False)
print(True+4)

