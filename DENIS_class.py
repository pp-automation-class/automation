class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        print("Animal sound")

class Dog(Animal):
    age = 10
    breed = "Labrador"
    color = "Brown"
    owner = "John"
    def woof(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Bird(Animal):
    age = 5
    breed = "Parrot"
    color = "Green"
    owner = "Jane"
    def tweet(self):
        print("Tweet")

my_animal = Animal("Rex")
print(my_animal.name)
my_animal.make_sound() # method call

my_dog = Dog("Bruno")
print(my_dog.name)
my_dog.woof() # method call
print(my_dog.age)
print(my_dog.breed)
print(my_dog.color)
print(my_dog.owner)
my_dog.age = 11
print(my_dog.age)

friend_dog = Dog("Rex")
print(friend_dog.name)
print(friend_dog.age)

my_cat = Cat("Whiskers")
print(my_cat.name)
my_cat.make_sound() # method call

my_bird = Bird("Tweetie")
print(my_bird.name)
my_bird.tweet() # method call
print(my_bird.age)
print(my_bird.breed)
print(my_bird.color)
print(my_bird.owner)