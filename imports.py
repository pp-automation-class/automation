# Ways to import in Python

# 1. import whole module
import math

print(math.sqrt(16))
print(math.pi)

# 2. import with alias
import datetime as dt

now = dt.datetime.now()
print(now)

# 3. import one name from a module
from random import randint

print(randint(1, 10))

# 4. import several names
from math import ceil, floor

print(ceil(4.2))
print(floor(4.8))

# 5. import name with alias
from math import pow as power

print(power(2, 3))

# 6. import your own file (same folder)
#    file must be named like variables.py → import variables
import variables

print(variables.APP_URL)
print(variables.port)

# 7. import one thing from your own file
from variables import username

print(username)

from classes import Dog
my_dog = Dog("Rex")
