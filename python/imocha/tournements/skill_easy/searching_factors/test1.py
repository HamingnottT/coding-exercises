def searchFactors(N,A):
    #this is default OUTPUT. You can change it
    result = 6%6, 8%6, 12%6
    
    # WRITE YOUR LOGIC HERE:    


    print(result)
    for i in A:
        print(i,end=" ")
        
#INPUT [uncomment & modify if required]
# temp = input().split()

# N = int(temp[0])
N = 6

A = []
# temp1 = input().split()
temp1 = 2, 6, 3, 4, 12, 8
for i in range(N):
    A.append(int(temp1[i]))

#OUTPUT [uncomment & modify if required]
searchFactors(N,A)