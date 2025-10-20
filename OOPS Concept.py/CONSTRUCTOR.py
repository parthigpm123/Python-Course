'''In Python, the term "constructor" typically refers to the special method __init__(). While __init__() is technically an initializer rather than a true constructor (which would handle object creation), it is the method responsible for setting up the initial state of an object when an instance of a class is created.'''

class Dog:
    def __init__(self, name, breed):
        """
        The constructor (initializer) for the Dog class.
        It initializes the 'name' and 'breed' attributes of a Dog object.
        """
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating instances of the Dog class, which automatically calls __init__()
my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Lucy", "Labrador")

print(f"My dog's name is {my_dog.name} and it's a {my_dog.breed}.")
my_dog.bark()

print(f"Your dog's name is {your_dog.name} and it's a {your_dog.breed}.")
your_dog.bark()