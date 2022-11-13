from sys import argv

script, filename = argv

print(f"we're going to erase the filename {filename}")
print("if you don't want to do that just hit hit CTRL-C (^C).")
print("if you want to do that hit return")
input("?")

print("opening file....")
target = open(filename, 'w')

target.truncate()
print("truncating file....goodbye")

print("now im going to ask you for 3 lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("im going to write to these files")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("finally we can close it")
target.close()
