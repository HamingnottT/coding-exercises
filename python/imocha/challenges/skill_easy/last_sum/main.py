def lastSum(N, A):
    A_to_stringlist = []

    # converts A to a string list so that picking out the last digit works without error
    # integers cannot normally be iterated through
    for i in A:
        A_to_stringlist.append(str(i))

    def lastSumHelper(N, A, Accum):
        if (N == 0): print(Accum)
        
        # recursively calls through stringlist
        # accumulator stores the last digit of each list index by converting the digit back to int type
        else: lastSumHelper(N - 1, A, int((A[N - 1])[-1]) + Accum)

    lastSumHelper(N, A_to_stringlist, 0)
   


# INPUT [uncomment & modify if required]

N = int(input())

temp = input().split()
A = []
for i in range(N):
    A.append(int(temp[i]))

# OUTPUT [uncomment & modify if required]
lastSum(N,A)