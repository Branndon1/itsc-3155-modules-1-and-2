num = []
even = []
num = input("Enter a number or QUIT to quit: ")
while True:
    num = input("Enter a number or QUIT to quit: ")
    if num.upper() == 'QUIT':
        break
    else:
        num.append(int(num))
        if int(num) % 2 == 0:
            even.append(int(num))

print("All nums:", num)
print("Even nums:", even)