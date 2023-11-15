# docs.python.org/3/library/functions.html#open
# 7:24:24 Harvard CS50’s Introduction to Programming with Python – Full University Course

names = []

# "r" may be omitted
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")