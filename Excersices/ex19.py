import random


def cheese_and_crackers(count, boxes):
  print(f"you have {count} cheeses")
  print(f"you have {boxes} boxes of crackers")
  print("Thats enough for a party")
  print("Get a blanket. \n")


print("we can just give the function numbers directly")
cheese_and_crackers(20, 30)

print("or we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do math inside too")
cheese_and_crackers(10 + 20, 5 + 6)

print("and we can combine the two, variables and math")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# Write atleast one more function of your own design, and run 10 different calls to that function.
def my_function(name, age):
  print(f"Hello {name}, you are {age} years old")


my_function("John", 20)

my_name = "bukhari"
my_age = 20

my_function(my_name, my_age)

age = input("how old are you? ")
name = input("what is your name? ")

my_function(name, age)


def assign_me_a_random_age(*args, **kwargs):
  agez = random.randint(0, 100)
  for arg in args:
    print(arg + " is " + str(agez) + " years old")

  for key, value in kwargs.items():
    print(key + " is " + str(agez) + " years old")


assign_me_a_random_age(
  "bukhari",
  "john",
  "jane",
  "joe"
)

assign_me_a_random_age(
  "bukhari"
)
