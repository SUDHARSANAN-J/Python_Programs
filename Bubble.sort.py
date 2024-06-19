def bubble_sort(n):

    while(n != sorted(n)):
        for i in range(0,len(n)-1):
            for j in range(i+1,i+2):
                if n[i] > n[j]:
                    n[i],n[j] = n[j],n[i]
    
    
                print(n)


n = list(map(int,input().split()))
print(n)
bubble_sort(n)




#[4,3,6,2,3,5,5]