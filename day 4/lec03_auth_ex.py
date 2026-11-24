# ---------------------------------------------------------------
# Concept: a tiny "Instagram-like" app that uses
#   1. a list of dictionaries as a simple in-memory database
#   2. a class (Auth) to hold users and the logged-in user
#   3. a decorator (login_required) to protect methods
# ---------------------------------------------------------------

# A list of dictionaries. Each dictionary is one "reel" (a video post).
# 'likes' is a number we can change later with reel['likes'] += 1
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
    # Class attributes: shared by every Auth object.
    # USERS         -> list of all registered user dictionaries
    # CURRENT_USER  -> the user who is logged in (None = nobody is logged in)
    USERS = []
    CURRENT_USER = None


    def register(self):
        # Ask the user for details and store them as a dictionary in USERS.
        print("\n--- Register a new user ---")
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        # self.USERS refers to the class-level list, so the new user is saved there
        self.USERS.append({"username":username, "email":email, "password": password})
        print(f"User '{username}' registered successfully!")
        print(f"Total registered users: {len(self.USERS)}")

    def login(self):
        # Ask for email and password, then look for a matching user.
        print("\n--- Login ---")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        # Check each stored user one by one
        for user in self.USERS:
            # Both email AND password must match
            if user.get('email') == email and user.get('password') == password:
                # Remember who is logged in, then stop searching
                self.CURRENT_USER = user
                print(f"Logged in as '{user.get('username')}'")
                break
            else:
                # Printed for every user that does not match (same as original logic)
                print("Invalid credentials!")


    # This is a DECORATOR function. It is NOT a method you call directly.
    # It takes a function (func) and returns a new function (wrapper) that
    # runs a check first and then calls the original function.
    def login_required(func):
        # wrapper replaces the original method, so it accepts self and any arguments
        def wrapper(self, *args, **kwargs):
            # Check: is someone logged in?
            if not self.CURRENT_USER:
                print("Login first!")
                return # function will stop here, the original method never runs
            # Someone is logged in, so run the original method.
            # NOTE: the original code uses *kwargs (single star) here, not **kwargs.
            # It is kept unchanged on purpose. Keyword arguments are not passed
            # correctly by this line, but the program never passes any keyword arguments.
            print(f"Access granted to '{func.__name__}'")
            return func(self, *args, *kwargs)

        return wrapper

    # @login_required means: like = login_required(like)
    # So calling like() first runs the login check inside wrapper.
    @login_required
    def like(self, reel_id):
        # Look through all reels and find the one with a matching id
        for reel in reels:
            if reel.get('id') == reel_id:
                print(reel)              # show the reel BEFORE the like
                reel['likes'] += 1       # add one like (changes the dictionary in place)
                print(reel)              # show the reel AFTER the like
        print("liked!")


# ---------------------------------------------------------------
# Main program: create an object and call its methods
# ---------------------------------------------------------------

# Create one Auth object. Its methods use the shared USERS list and CURRENT_USER.
Insta = Auth()

# Step 1: register a user (asks for username, email, password)
Insta.register()

# Step 2: log in with the email and password you just registered
Insta.login()

# Step 3: like some reels.
# Each call goes through login_required first.
# If no user is logged in, the wrapper prints "Login first!" and stops.
print("\n--- Liking reels ---")
Insta.like('0001')
Insta.like('0002')
Insta.like('0001')   # liking 0001 again, so its count goes up again
Insta.like('0005')
Insta.like('0003')
Insta.like('0002')
