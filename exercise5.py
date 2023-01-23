list1 = []
list2 = []
print("Enter five numbers for the first list: ")
for i in range(5): 
    num = int(input())
    list1.append(num)
print("Enter five numbers for the second list: ")
for i in range(5): 
    num = int(input())
    list2.append(num)

common = list(set(list1) & set(list2))

print("First list: ", list1)
print("Second list: ", list2)
print("Common list: ", common)