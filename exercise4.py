n = int(input("Enter a number: "))
list = []
for i in range(n): list.append(float(input("enter a float: ")))
mean = sum(list) / len(list)
print("List: ", list)
print("Mean:", mean)