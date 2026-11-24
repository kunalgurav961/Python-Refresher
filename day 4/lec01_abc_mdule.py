from abc import ABC, abstractmethod

# ABC = AbstractBaseClass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self, rad):
        return 3.14 * rad * rad

cir = Circle()
print(cir.area(3.4))