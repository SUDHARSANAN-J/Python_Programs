n = int(input("Enter a number : "))
sum = 0
a = str(n)

for i in a:
    digit = int(i) ** 3
    sum = sum + digit
print(sum)