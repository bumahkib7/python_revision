def printTwo(*args):
  arg1, arg2 = args
  print(f"arg1: {arg1}, arg2: {arg2}")


def printTwoAgain(arg1, arg2):
  print(f"arg1: {arg1}, arg2: {arg2}")


def printOne(arg1):
  print(f"arg1: {arg1}")


def printNone():
  print("I got nothing")


printTwo("Zed", "Shaw")
printTwoAgain("Zed", "Shaw")
printOne("First!")
printNone()


def print_food(*args):
  for arg in args:
    print(arg)


print_food("pizza", "burger", "hotdog")


def print_food1(food1, food2, food3):
  print(f"food1: {food1}")
  print(f"food2: {food2}")
  print(f"food3: {food3}")


print_food1(food1="pizza", food2="burger", food3="hotdog")
