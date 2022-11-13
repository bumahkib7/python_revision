def add(a, b):
  print(f"ADDING {a} + {b}")
  return a + b


def subtract(a, b):
  print(f"SUBTRACTING {a} - {b}")
  return a - b


def multiply(a, b):
  print(f"MULTIPLYING {a} * {b}")
  return a * b


def divide(a, b):
  print(f"DIVIDING {a} / {b}")
  return a / b


def modulo(a, b):
  print(f"MODULO {a} % {b}")
  return a % b


print("Let's do some math with just functions!")

age = add(int(input()), int(input()))
height = subtract(78, 4)
weight = multiply(int(input()), int(input()))
iq = divide(100, 2)
mod = modulo(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}, Mod: {mod}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# Study Drills
# 1. If you aren't really sure what return does, try writing a few of your own functions and have them return some values. You can return anything that you can put to the right of an =

# 2. At the end of the script is a puzzle. I'm taking the return value of one function and using it as the argument of another function. I'm doing this in a chain so that I'm kind of creating a formula using the functions. It looks really weird, but if you run the script, you can see the results. What you should do is try to figure out the normal formula that would recreate this same set of operations.

# 3. Once you have the formula worked out for the puzzle, get in there and see what happens when you modify the parts of the functions. Try to change it on purpose to make another value.

# 4. Do the inverse. Write a simple formula and use the functions in the same way to calculate it.

# 5. And finally, do the simplest math you can do to figure out how to convert the inches and pounds to centimeters and kilograms. If you can't do it on paper, try to do it in Python anyway.

# 6. Write a function that takes a list of numbers and returns the largest number in the list. Do not use the built-in max() function.

# 7. Write a function that takes a list of words and returns the length of the longest one.

# 8. Write a function that takes a list of numbers and returns a new list with all the elements doubled.

# 9. Write a function that takes a list of strings and a new string containing all the strings concatenated together. For example, if the list was ['Hello', 'world'] and the separator was ', ' the result should be 'Hello, world'.
