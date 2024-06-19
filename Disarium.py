n = input()
b = 0
sum = 0

for i in n:
    b = b + 1
    c= int(i) ** b
    sum = sum + c
if (sum == int(n)):
    print(n, "is a disarium")
else:
    print(n, "is not a disarium")