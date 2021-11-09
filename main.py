numbers = input("Insert odd and even numbers: ")
list = []

x = numbers.split()
for num in x:
    if int(num) % 2 == 1:
        list.append(num)

print(list)
