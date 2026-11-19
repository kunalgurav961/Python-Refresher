'''
Note: In Python, “protected” is only a naming convention, not something the language enforces. A single leading underscore (_xyz) tells other programmers “this is internal, please don’t touch it from outside,” but the interpreter does nothing to stop you. That’s why print(d._xyz) works fine.
'''


class Animal:
    ''' parent class '''
    _xyz = 'lasdkjflkjdf'

    def __init__(self, name):
        self.name = name # Animal's property
    def speak(self):
        print("animal speaking...")

class Dog(Animal):
    ''' child class '''

    def __init__(self, name, age):
        super().__init__(name)
        self.name = 'Dog 1'
        self.age = age # dog's property
    def eat(self):
        print("eating...")

d = Dog("Sheru", 12)
print(d.name, d.age)
