import math

def carArrangement(N, A):
    # this is default OUTPUT. You can change it.
    mod_res = ""
    mod_counter_0 = 0
    mod_counter_1 = 0

    try:
        for A[i] in A: # range(0, len(A))
            if (A[i] % 2 == 0):
                mod_counter_0 += 1

        for A[i] in range(0, len(A)):
            if (A[i] % 2 == 1):
                mod_counter_1 += 1

        # for A[i] in A: # range(0, len(A))
        #     if (A[i] == 1):
        #         # mod_counter_1 += -1
        #         pass

    except ZeroDivisionError:
        mod_counter_0 += 1
    finally:
        pass

    result = f"{abs(mod_counter_1)} {round(mod_counter_0/2)}"

    # write your Logic here:

    return result


# INPUT [uncomment & modify if required]

# N = int(input())
N = 3

# temp = input().split()
temp = "0 0 0".split()
A = []
for i in range(N):
    A.append(int(temp[i]))

# OUTPUT [uncomment & modify if required]
print(carArrangement(N,A))