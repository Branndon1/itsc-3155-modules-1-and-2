string = input("Enter a string: ")

list = [list(string[n:n+3]) for n in range(0, len(string), 3)]

print(list)