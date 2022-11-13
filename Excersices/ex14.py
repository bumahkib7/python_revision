from sys import argv

script, user_name, first_name, last_name = argv

prompt = '>>>'

print(f"hi {user_name}, I'm the {script} script.".capitalize())
print("i'd like to ask you a few questions.".capitalize())
print(f"do you like me {user_name}?".capitalize())
likes = input(prompt)

print(f"where do you live {user_name}?".capitalize())
lives = input(prompt)

print(f"what kind of computer do you have?".capitalize())
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a computer {computer}. Nice
""")

print(f" your name is {first_name}, {last_name}")
