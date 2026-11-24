# Outer function
def login_required(func):
    # Inner function
    def wrapper(*args, **kwargs):
        print("Before calling the func")
        res = func(*args, **kwargs)
        print("After calling function")
        return res
    return wrapper

@login_required
def info(**data):
    print(f"Hello, I am {data.get('name')}.\nI live in {data.get('city')}")
    return 200
    # print(data)

info(name="kunal", age=23, city='pune')

def add(*nums):
    total = 0
    for i in nums:
        total += i
    return total

# print(add(3, 4, 5, 6, 7, 8, 9))
