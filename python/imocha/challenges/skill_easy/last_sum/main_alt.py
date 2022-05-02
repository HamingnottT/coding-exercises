# alternative way of expressing lastSum's recursion
# this is closer to the predefined boilerplate with now a recursive function called to convert A to a string list

def lastSum(N, A):
    A_to_stringlist = []

    # recursive call to convert A to a string list
    # integers cannot normally be iterated through
    def AToStringlist(N, A_input, Accum):
        if (N == 0): return Accum.split()   # splits the concatenated string into a list
        
        # recursively calls through conversion function
        # accumulator converts each index of A to string, then concatenates each string index into one single merged string - the space delimits each number
        else: return AToStringlist(N - 1, A_input, str(A_input[N-1]) + " " + Accum)

    A_to_stringlist = AToStringlist(N, A, "")

    def lastSumHelper(N, stringList, Accum):
        if (N == 0): return Accum
        
        # recursively calls through stringlist
        # accumulator stores the last digit of each list index by converting the digit back to int type
        else: return lastSumHelper(N - 1, stringList, int((stringList[N - 1])[-1]) + Accum)

    result = lastSumHelper(N, A_to_stringlist, 0)
    return result
   


# INPUT [uncomment & modify if required]

N = int(input())

temp = input().split()
A = []
for i in range(N):
    A.append(int(temp[i]))

# OUTPUT [uncomment & modify if required]
print(lastSum(N,A))