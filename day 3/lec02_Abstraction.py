class Shape:
    def __init__(self, dim):
        self.dim = dim

    def magic_func(self):
        '''
            complex implementation here
        '''
        print("Jaaaddoooooo")

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, pi, r):
        super().__init__({
            "pi": pi,
            "rad": r
        })
        print(f"Circle having {self.dim.get('rad')} radius has been creaded!")

    def area(self):
        return self.dim.get('pi') * self.dim.get('rad') * self.dim.get('rad')
    
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__({"base": base, "height": height})

    def area(self):
        return 0.5 * self.dim.get("base") * self.dim.get('height')

cir = Circle(3.14, 3.5)
tri = Triangle(5, 2.4)
cir.magic_func()