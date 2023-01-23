list = []
print("Enter 5 words: ")
for i in range(5):
    list.append(input())

string = " ".join(list)

print("Words:", list)
print("One string:", string)