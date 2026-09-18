# Ways to import in Python

# import the whole module
import math
print(math.sqrt(16))
print(math.pi)

# import with a short name
import random as rnd
print(rnd.randint(1, 6))

# import one thing from a module
from datetime import date
print(date.today())

# import several things
from math import ceil, floor
print(ceil(3.2))
print(floor(3.8))

# import your own file (same folder, no .py in the name)
from DENIS_class import Dog
my_dog = Dog("Bruno")
print(my_dog.name)
my_dog.woof()

from DENIS_class import Dog
my_dog = Dog("Bruno")