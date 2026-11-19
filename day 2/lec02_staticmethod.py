# dunder methods
# usually starts with __ and ends with __
print("========= Output ==========")
class Dog:
    # constructor
    def __init__(self, name):
        self.name = name
        
    # Decorator
    @staticmethod
    def speak():
        '''If we want to call this function without using the object'''
        print("dog is barking...")
    def eat(self):
        print(f"{self.name} Eat!")
    def __str__(self):
        return f'''I am {self.name}.'''

d1 = Dog("Sheru")
# print("name:", d1.name)
# d2 = d1 # d2 holds a copy instance of d1
# print(d2.name)

# Dog.eat(d1)
Dog.speak()
