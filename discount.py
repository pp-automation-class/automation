age = int(input("Enter your age: "))
# for 18 and less discount is 10%
# for more than 18 to 64 discount is 5%
# for 60 and more discount is 15%

if age <= 21:
    print(10)
if age > 21 and age > 65:
    print(5)
else:
    print(35)
or
and

#And
True and True = True
True and False = False
False and True = False
False and False = False

#Or
True or True = True
True or False = True
False or True = True
False or False = False

#Not