reels = [
    {
    'id': '0001',
    'title': 'Nvidia Ceo',
    'likes': 0,
}, {
    'id': '0002',
    'title': 'Morning coffee latte art',
    'likes': 124,
}, {
    'id': '0003',
    'title': 'Quick 5-minute stretch routine',
    'likes': 857,
}, {
    'id': '0004',
    'title': 'Sunset timelapse from the terrace',
    'likes': 2310,
}, {
    'id': '0005',
    'title': 'Cat tries to catch a laser dot',
    'likes': 9642,
}, {
    'id': '0006',
    'title': 'Python tip: list comprehensions in 30 seconds',
    'likes': 415,
}]

class Auth:
    USERS = []
    CURRENT_USER = None


    def register(self):
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.USERS.append({"username":username, "email":email, "password": password})

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for user in self.USERS:
            if user.get('email') == email and user.get('password') == password:
                self.CURRENT_USER = user
                break
            else:
                print("Invalid credentials!")

    
    def login_required(func):
        def wrapper(self, *args, **kwargs):
            if not self.CURRENT_USER:
                print("Login first!")
                return # function will stop here
            return func(self, *args, *kwargs)

        return wrapper

    @login_required
    def like(self, reel_id):
        for reel in reels:
            if reel.get('id') == reel_id:
                print(reel)
                reel['likes'] += 1
                print(reel)
        print("liked!")


Insta = Auth()
Insta.register()
Insta.login()
Insta.like('0001')
Insta.like('0002')
Insta.like('0001')
Insta.like('0005')
Insta.like('0003')
Insta.like('0002')