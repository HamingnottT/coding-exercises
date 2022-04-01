def gameWinner(N, A, B):
    
    print(A)
    print(B)

    counter = 0
    A_score = 0
    B_score = 0

    
    # print(A[len(A)-1])

    # for A[i] in A:
    #     A[i-1]
    #     A_score += 1

    while (counter != N):
        counter += 1
        if (A[counter-1] > B[counter-1]):
            A_score += 1
            counter
        elif (B[counter-1] > A[counter-1]):
            B_score += 1
        elif (B[counter-1] == A[counter-1]):
            A_score += 1
            B_score += 1
        else:
            pass

    print(A_score)
    print(B_score)

    result = "placeholder"
    return result

# INPUT [uncomment & modify if required]

# N = int(input())
N = 5

# temp = input().split()
temp = "4 7 3 2 9".split()
A = []
for i in range(N):
    A.append(int(temp[i]))

# temp_1 = input().split()
temp_1 = "6 9 2 6 3".split()
B = []
for i in range(N):
    B.append(int(temp_1[i]))

# OUTPUT [uncomment & modify if required]
print(gameWinner(N, A, B))

# def sortArray(N, A):
#     # this is default OUTPUT. You can change it.
#     result = -404

#     # write your Logic here:

#     return result