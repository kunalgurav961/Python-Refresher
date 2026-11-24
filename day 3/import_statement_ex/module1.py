import random
import string


def greet(name="friend"):
    """Print a greeting for the given name."""
    print(f"Hello, {name}!")


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def roll_dice(sides=6):
    """Return a random number from 1 to sides."""
    return random.randint(1, sides)


def random_password(length=12):
    """Generate a random password of letters and digits."""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def flip_coin():
    """Return 'Heads' or 'Tails' at random."""
    return random.choice(["Heads", "Tails"])


def reverse_string(text):
    """Return the text reversed."""
    return text[::-1]


def count_vowels(text):
    """Count the vowels in a string."""
    return sum(1 for ch in text.lower() if ch in "aeiou")


def is_palindrome(text):
    """Check whether text reads the same forwards and backwards."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


def random_color():
    """Return a random hex color code."""
    return "#" + "".join(random.choice("0123456789ABCDEF") for _ in range(6))


if __name__ == "__main__":
    print(__name__)

    print(random_color())