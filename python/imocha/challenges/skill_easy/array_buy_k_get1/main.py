def BKG1(N, K, A):
    
    A_sort_desc = sorted(A, reverse=True)

    del A_sort_desc[K]
    
    result = sum(A_sort_desc)

    return result

#INPUT [uncomment & modify if required]
n,k = map(int, input().split())
result = -404; 
A = list(map(int, input().split()))


#OUTPUT [uncomment & modify if required]
print(BKG1(n, k, A))