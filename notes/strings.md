# Python String & Immutability Notes

## 1. What is a String?

A string is an immutable sequence of characters in Python.

Example:
name = "alina"

Strings are enclosed in:
- Single quotes ''
- Double quotes ""
- Triple quotes ''' '''

---

## 2. Indexing

Each character has an index.

Example:
name = "alina"

Index positions:
a  l  i  n  a
0  1  2  3  4

Access character:
name[0] → 'a'
name[2] → 'i'

---

## 3. Slicing

Slicing extracts part of a string.

Syntax:
string[start:end]

Example:
name = "alina"

name[1:] → "lina"
name[:3] → "ali"
name[0:4] → "alin"

---

## 4. Strings Are Immutable

Strings cannot be modified after creation.

Wrong:
name = "alina"
name[0] = "A"   # Error

Error:
TypeError: 'str' object does not support item assignment

Reason:
Strings are immutable objects.

---

## 5. Correct Way to Modify String

We create a new string.

Example:
name = "alina"
name = "A" + name[1:]

Result:
"Alina"

This does NOT modify the old string.
It creates a new string and reassigns the variable.

---

## 6. String Methods Return New Objects

Example:
s = "hello"
s = s.upper()

.upper() does NOT change original string.
It returns a new string.

---

## 7. += Operator with Strings

a = "python"
a += "3"

This means:
a = a + "3"

It creates a new string:
"python3"

---

## 8. Identity vs Equality

==  → Checks value
is  → Checks memory location

Example:
a = "hi"
b = a

a is b → True (same object)

a = a + "!"
a is b → False (new object created)

---

## 9. Important Memory Concept

When modifying strings:
- Python creates a new object
- Variables change reference
- Old string remains if another variable points to it

Example:
s = "hello"
t = s
s = s.upper()

Now:
s → "HELLO"
t → "hello"