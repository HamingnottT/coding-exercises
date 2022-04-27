def minimumCost(N,M,A):
    

    if (M == 1):
        result = A[0] + A[-1]

    else:
        pass

        # these cause an error - need to look further into
        # split_arr1 = A[round(len(A)\2):-1]

        # split_arr2 = A[0:round(len(A)\2)]
    
    
    #WRITE YOUR LOGIC HERE:
    
    
    print(result)

#INPUT [uncomment & modify if required]

# test input
# 10 1
# 100 1 4 2 9 1 2 60 38 11

# 5 2
# 2 2 2 2 2

# 3 1
# 1 2 3

temp = input().split()

N = int(temp[0])
M = int(temp[1])
A = list(map(int,input().split()))

#OUTPUT [uncomment & modify if required]
minimumCost(N,M,A)