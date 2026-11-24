# Remove Vowels from a String (Recursion)

## Question

Write a function that takes a string as a parameter and deletes the vowels from it.

Constraints:

- Do not use a loop.
- Do not import any module.
- Do not use `str.translate` or `str.maketrans`.

## Idea

A string can be split into two parts:

- its **first character**, `s[0]`
- the **rest of the string**, `s[1:]`

The vowels in the whole string are the vowels in the first character plus the vowels in the rest. So the function can solve the problem for the rest of the string by calling itself. This is **recursion**.

Two rules are needed:

1. **Base case:** if the string is empty, there is nothing to do, so return an empty string.
2. **Recursive case:**
   - If the first character is a vowel, drop it and process the rest: `remove_vowels(s[1:])`.
   - Otherwise, keep the first character and put it in front of the processed rest: `s[0] + remove_vowels(s[1:])`.

## Solution

```python
def remove_vowels(s):
    if s == "":
        return ""
    if s[0] in "aeiouAEIOU":
        return remove_vowels(s[1:])
    return s[0] + remove_vowels(s[1:])

print(remove_vowels("Hello World"))  # Hll Wrld
```

## How it runs on `"Hello World"`

Each call handles one character and passes the rest to the next call:

| Call | First character | Action | Returns so far |
|------|-----------------|--------|----------------|
| `remove_vowels("Hello World")` | `H` | not a vowel, keep it | `H` + ... |
| `remove_vowels("ello World")` | `e` | vowel, drop it | ... |
| `remove_vowels("llo World")` | `l` | keep it | `l` + ... |
| `remove_vowels("lo World")` | `l` | keep it | `l` + ... |
| `remove_vowels("o World")` | `o` | vowel, drop it | ... |
| `remove_vowels(" World")` | ` ` | not a vowel, keep it | ` ` + ... |
| `remove_vowels("World")` | `W` | keep it | `W` + ... |
| `remove_vowels("orld")` | `o` | vowel, drop it | ... |
| `remove_vowels("rld")` | `r` | keep it | `r` + ... |
| `remove_vowels("ld")` | `l` | keep it | `l` + ... |
| `remove_vowels("d")` | `d` | keep it | `d` + ... |
| `remove_vowels("")` | - | base case, return `""` | |

When the calls return, the kept characters are joined in order: `H l l` + ` ` + `W r l d` gives `Hll Wrld`.

## Key points

- A recursive function must have a **base case**, or it calls itself forever.
- `s[1:]` is a slice that gives everything after the first character. Each call makes the string shorter, so it reaches the base case.
- Recursion replaces the loop here: each call does one character's work and hands the rest to the next call.
