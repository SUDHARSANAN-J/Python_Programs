
def fact(n, sum):
    if (n >= 1):
        for i in range(1,n+1):
            sum = sum * i
        print(sum)

    else:
        print("not a positive number")

n = int(input("Enter a number : "))
sum = 1

fact(n, sum)
