list1 = []
print("Enter 10 numbers: ")
for i in range(10):
    num = int(input())
    list1.append(num)

list2 = list(set([i for i in list1 if list1.count(i) == 1]))

print("Original list:", list1)
print("New list:", list2)