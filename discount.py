age = int(input("Enter your age: "))

# for 18 and less discount 10% 
# for more then 18 to 64 discount 5%
# for 65 and more discount 15%

# if age <= 18:
#     print(10)
if age < 18 or age > 65:
    print(5)
# else:
#     print(15)



# And
True and True = True
True and False = False
False and True = False
False and False = False

# Or
True or True = True
True or False = True
False or True = True
False or False = False

# Not
True = False