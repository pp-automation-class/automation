class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        print("Animal sound")

class Dog(Animal):
    age = 10
    breed = "Labrador"

    def woof(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# my_animal = Animal("Rex")        
# print(my_animal.name)
# my_animal.make_sound()

my_dog = Dog("Bruno")
print(my_dog.name)
my_dog.woof()
print(my_dog.age)
print(my_dog.breed)
my_dog.age = 11
print(my_dog.age)

friends_dog = Dog("Rex")
print(friends_dog.name)
print(friends_dog.age)


# my_cat = Cat("Whiskers")
# print(my_cat.name)
# my_cat.make_sound()