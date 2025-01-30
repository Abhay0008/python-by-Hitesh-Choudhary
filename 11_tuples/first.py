# tuples in python

# tuple is similar to list but tuple is immutable while list is mutable

tea_type = ("black","green","white","black")
print(tea_type)
print(tea_type[1])
print(tea_type[-1])
print(tea_type[1:])
# tea_type[0]="lemon"# will give error bcoz tuple is immutable , tuple object doesnot support item assignment

print(len(tea_type))
coffee_type = ("brugold","nestle")
tea_cof=tea_type+coffee_type
print(tea_cof)
print(coffee_type)

if "brugold" in tea_cof:
    print("brugold is present in tea_cof")

print(tea_cof.count("black"))# will give no. of occurances

(kala,haraa,safed,kala)=tea_type # assigning items of tuple to variables
print(kala)
print(safed)

new_tup = (" shdf",12,("dfs",43))
print(new_tup)
print(new_tup[2])

