# dictionaries in python

chai_types = {'masala':"spicy",'ginger':"zesty",'green':"mild"}
# print(chai_types)
# print(chai_types['masala'])
# print(chai_types.get('green'))
# # print(chai_types['ding'])#will give error bcoz ding key is not in dict
# chai_types['green']="fresh"
# print(chai_types)

# # dictionary iteration

# for chai in chai_types:
#     print(chai,end=", ") #will print only keys
# print("\n")
# for chai in chai_types:
#     print(chai, chai_types[chai])


# for key, value in chai_types.items():
#     print(key,value)

# if "masala" in chai_types:
#     print("masala chai is present")

# print(len(chai_types))

# ## adding single element in dict.. in end

# chai_types['new chai']="MMM chai"

# print(chai_types)

# #poping item from dict using the key

# # chai_types.pop('new chai')
# # print(chai_types)

# chai_types.popitem()#will pop one item from end
# print(chai_types)

# chai_copy=chai_types.copy()
# print(chai_copy)
# del chai_copy['green'] # deletes given key
# print(chai_copy)
# print(chai_types)


## dictionary of dict..

# tea_shop = {'masala':"spicy chai",'coffe':{'new':"bruGold",'old':"nestle"}}
# print(tea_shop)
# print(tea_shop['coffe']['new'])
# print(tea_shop['coffe']['old'])

# square_num = {x:x**2 for x in range(5)}
# print(square_num)

# square_copy=square_num
# print(square_copy)
# square_copy.clear() # clear() method for clearing a dict...
# print(square_copy)

## another way of creating a dict..

keys = ['masala','ginger','black','lemon']
default_tea="kadak"
new_dict= dict.fromkeys(keys,default_tea)
# new_dict= dict.fromkeys(keys,keys)# in this case value will be whole keys list
print(new_dict)
