# class Car:
#     # Data
#     price = "1Lakh"
#     # Methods
#     def move(self):
#         print(self)

#     def __init__(self, name, price):
#         self.name = name
        

# # object
# # syntax: obj_name = class_name()
# bmw = Car("bmw", "1Lakh")
# lambo = Car()
# bmw.move()
# print(bmw)


class Student:
    # class variable
    SCHOOL = 'xyz'
    COLLEGE = 'mit'
    def __init__(self, name, roll):
        # Instance variable
        self.name = name
        self.roll = roll
    
    def info(self):
        print(f"name-> {self.name}")
        print(f"roll-> {self.roll}")


pratham = Student("Prathamesh", 10001)
kunal = Student("Kunal", 10002)
priya = Student("Priya", 10003)
kunal.age = 34 # instance variable
print(priya.SCHOOL)
print(kunal.SCHOOL)
print(pratham.SCHOOL)

pratham.SCHOOL = 'abc'
print('kunal school', kunal.SCHOOL)
print(pratham.SCHOOL)