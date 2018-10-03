base_height = int(input("Enter arrow base height:\n"))
base_width = int(input("Enter arrow base width:\n"))
head_width = int(input("Enter arrow head width:\n"))

# continue prompting for input if the head width is shorter than the base width
while head_width <= base_width:
    head_width = int(input("Enter arrow head width:\n"))

# print a newline for zybooks whitespace requirements
print()

for i in range(base_height):
    for j in range(base_width):
        print('*', end='')
    print()
for i in reversed(range(head_width)):
    for j in range(i + 1):
        print('*', end='')
    print()
