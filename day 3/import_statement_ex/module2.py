# write a function that takes a string as an parameter to delete the vowels from the string.(without using loop)
def remove_vowels(s):
    if s == "":
        return ""
    if s[0] in "aeiouAEIOU":
        return remove_vowels(s[1:])
    return s[0] + remove_vowels(s[1:])

print(remove_vowels("Hello World"))  # Hll Wrld