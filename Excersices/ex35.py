def gold_room():
  print("this room is full of gold. how much do you take?")


choice = ">>>>>"

if "0" or "1" in choice:
  how_much = int(choice)
else:
  dead("Man, learn to type a number.")
  if how_much < 50:
    print("Nice, you're not greedy, you win!")
    exit(0)
  else:
    dead("You greedy bastard!")


def bear_room():
  print("There is a bear here.")
  print("The bear has a bunch of honey.")
  print("The fat bear is in front of another door.")
  print("How are you going to move the bear?")
  bear_moved = False


while True:
  choice = input("> ")

  if choice == "take honey":
    dead("The bear looks at you then slaps your face off.")
  elif:
    choice == "taunt bear" and not bear_moved:
    print("The bear has moved from the door.")
  print("You can go through it now.")
  bear_moved = True
elif:
choice == "taunt bear" and bear_moved: \
  dead("The bear gets pissed off and chews your leg off.")
elif:
choice == "open door" and bear_moved: gold_room()
else:
print("I got no idea what that means.")


def dead(Why):
  print(Why, "Good Job!")
