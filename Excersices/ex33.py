def while_looping():
  ib = 0;
  numbers = []
  while ib < 6:
    print(f"At the top of i is {ib}")
    numbers.append(ib)

    ib += 1
    print("Numbers now: ", numbers)

    print(f"At the bottom is {ib}")

  print("the numbers: ".capitalize())

  for num in numbers:
    print(num)


while_looping()
