def prime(input1):
        ls = []
        count = 0

        for i in range(2,50+1):
            for j in range(1,i+1):
                if (i % j == 0):
                    count = count + 1
            if ( count == 2 ):
                ls.append(i)
                print(ls)
                count = 0
            else:
                 count = 0
        
        a = ls[input1-1]
        print (a)

input1 = int(input())
prime(input1)