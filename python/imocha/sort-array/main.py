def sortArray(N, A):
    
    # N should be used to bind to list A for better ordering
    # map_N_to_A = map(N, A)
    # print(map_N_to_A)

    # maps list A into string
    string_A_val = map(str, A)

    # finds the maximum length of list A
    max_A_length = max(map(len, string_A_val))

    # sorts list A by the maximum index length - right justified returns order by instance starting from reverse order
    sort_A_2 = sorted(A, key = lambda index: (str(index).rjust(max_A_length, 'a')))
    # output [1290, 122, 10, 8, 9]

    # reverse the output of the above sort function
    r_sort_A_2 = sort_A_2[::-1]
    # output [9, 8, 10, 122, 1290]

    # converts the above list to string
    string_A = str(r_sort_A_2)

    # container for unwanted characters
    unwanted_chars = "[,]"

    # for-loop to filter out the unwanted list characters
    for char in unwanted_chars:
        string_A = string_A.replace(char, "")
    # output 9 8 10 122 1290
    
    result = string_A
    # result = string_A[1:-1]

    return result


# INPUT [uncomment & modify if required]

# N = int(input())

# temp = input().split()
A = []

# custom input
N = 4
temp = "237 23 11121 82".split()

for i in range(N):
    A.append(int(temp[i]))

# OUTPUT [uncomment & modify if required]
print(sortArray(N,A))