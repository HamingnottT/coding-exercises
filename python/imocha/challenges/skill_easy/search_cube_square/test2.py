#  /!\ input results in traceback error at for loop input
import re


def cubeSquare(T,N):
    # aux functions to find square root and cube root
    def sq_root(number):
        return number ** (1/2)

    def cub_root(number):
        return number ** (1/3)

    raw_cube = []
    raw_square = []
    cube_list_dict = {}
    boolean_container = []
    N_to_int = []

    # recursion to iterate thru N integer list
    def getSquareList(numInput, accum):
        if (N == 0): return accum
        else: return getSquareList(numInput - 1, accum.append[sq_root(numInput)])

    for i in N_to_int:
        print(getSquareList(i, []))


    result = T, N_to_int

    return result

#INPUT [uncomment & modify if required]
T = int(input())
N = []

for i in range(0, T):
    N.append(input())

# /!\ original input loop - causes errors
# for i in range(T):
# 	N.append(int(input[i]))

        
#OUTPUT [uncomment & modify if required]
print(cubeSquare(T,N))