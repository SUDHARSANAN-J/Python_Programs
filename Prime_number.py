n = int(input("Enter a number : "))
sum = 0

if (n >= 2):
    for i in range (1, n+1):
        if (n % i == 0):
            sum = sum + 1


if (n == 2):
    print(n,"is a composite")
elif (sum == 2):
    print(n,'is a prime')
else:
    print("not a prime")

