'''In Python, "method type" primarily refers to the three distinct categories of methods found within classes:
Instance Methods:
These are the most common type of methods.
They operate on a specific instance (object) of a class.
They take self as their first parameter, which refers to the instance itself, allowing them to access and modify instance-specific attributes.
Python'''

class MyClass:
        def __init__(self, value):
            self.value = value

        def get_value(self):  # Instance method
            return self.value
'''Class Methods:
These methods operate on the class itself, rather than a specific instance.
They are defined using the @classmethod decorator.
They take cls as their first parameter, which refers to the class, allowing them to access and modify class-level attributes.
They can be called directly on the class or on an instance of the class.
Python'''

class MyClass:
        class_attribute = 0

        @classmethod
        def increment_class_attribute(cls):  # Class method
            cls.class_attribute += 1
'''Static Methods:
These methods are similar to regular functions but are defined within a class for organizational purposes.
They are defined using the @staticmethod decorator.
They do not take self or cls as their first parameter and cannot access instance-specific or class-specific data.
They are essentially utility functions that logically belong to the class but don't require any class or instance state.
Python'''

class MyClass:
        @staticmethod
        def greet(name):  # Static method
            return f"Hello, {name}!"
      
'''Understanding these different method types is crucial for effective object-oriented programming in Python, as each serves a distinct purpose in managing data and behavior within classes.'''