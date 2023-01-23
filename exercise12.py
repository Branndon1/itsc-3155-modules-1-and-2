string = input("Enter a string: ")
lowercase = ""
other = ""

for char in string:
    if char.islower():
        lowercase += char
    elif char != " ":
        other += char

print(lowercase + other)