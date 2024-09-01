ls1 = list(map(str,input().split()))
ls2 = list(map(str,input().split()))
count = 0

print(ls1)
print(ls2)

for i in ls1:
    for j in ls2:
        if(i == j):
            count += 1

if(count == len(ls1)):
    print("true")
else:
    print("false")