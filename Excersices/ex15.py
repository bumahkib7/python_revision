from sys import argv

script, filename = argv
text = open(filename)

print(f"here is your filename {filename}:")
print(text.read())
