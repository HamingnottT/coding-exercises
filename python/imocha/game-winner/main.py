def gameWinner(N, A, B):
    
    # print(A)
    # print(B)

    counter = 0
    A_score = 0
    B_score = 0
    winning_list = ""
    result = ""

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

    if (A_score > B_score):
        winning_list = "A"
        result = f"{winning_list} {A_score}"
    elif (B_score > A_score):
        winning_list = "B"
        result = f"{winning_list} {B_score}"
    else: 
        winning_list = "tied"
        result = winning_list

    return result

# INPUT [uncomment & modify if required]

N = int(input())
# N = 5

temp = input().split()
# temp = "4 7 3 2 9".split()

A = []
for i in range(N):
    A.append(int(temp[i]))

temp_1 = input().split()
# temp_1 = "6 9 2 6 3".split()
B = []
for i in range(N):
    B.append(int(temp_1[i]))

# OUTPUT [uncomment & modify if required]
print(gameWinner(N, A, B))