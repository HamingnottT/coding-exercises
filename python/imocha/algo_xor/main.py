def mergedArray(N,A,B):
    #this is default OUTPUT. You can change it

    # merge both lists into list A
    for i in range(len(B)):
        A.append(B[i])
    
    # Bitwise XOR operation on merged list A
    result = max(A) ^ min(A)

    return result

#INPUT [uncomment & modify if required]
N=int(input())
A=[]
B=[]

temp=input().split()
for i in range(N):
    A.append(int(temp[i]))    

temp=input().split()
for j in range(N):
    B.append(int(temp[j]))
#OUTPUT [uncomment & modify if required]
print(mergedArray(N,A,B))