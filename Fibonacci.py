num1 = 0
num2 = 1

print("Fibonacci series from 0 to 100 :")
print(num1)
print(num2)

for i in range(0,100):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3)
    