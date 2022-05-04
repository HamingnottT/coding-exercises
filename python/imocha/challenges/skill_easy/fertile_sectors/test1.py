"""
What do I know?
1. Sectors are 2 cells by 2 cells, totalling four values per cell
2. In the sector atleast one pair should be divisible by 4
3. N * 4 is how many pairs there are
4. A is a matrix
"""

def test1(N, A):
    print(f"debug show input variables: {N, A}")
    print(f"debug sample sector: {A[0][0] + A[0][1], A[1][0]+ A[1][1]}")
    # print(A[3],A[4])
    # print(A[- len(A) + 3], A[- len(A) + 4])

    # print(A[-len(A)][-len(A) + 1])

    print((A[- N][- N] + A[- N][- N + 1]), (A[- N + 1][- N] + A[- N + 1][- N + 1]))

    print((A[- 1][- 1], A[- 1][- 1 + 1]), (A[- 1 + 1][- 1], A[- 1 + 1][- 1 + 1]))

    M = 3

    toptwo = (A[- M][- M] + A[- M][- M + 1]) % 4
    bottomtwo = (A[- M + 1][- M] + A[- M + 1][- M + 1]) % 4

    # assessor = 0
    # if toptwo % 4 == 0: assessor += 1
    # if bottomtwo % 4 == 0: assessor += 1
    # print(assessor)

    toptwohelperA = 0
    toptwohelperB = 1

    bottomtwohelperA = 3
    bottomtwohelperB = 4

    def fertile_sector_array(N, toptwo, bottomtwo, accumulator):
        if N == 0: return accumulator
        else: 
            print(N, toptwo, bottomtwo, accumulator)
            if toptwo + bottomtwo % 4 == 0: accumulator += 1
            # if bottomtwo % 4 == 0: accumulator += 1
            try:
                return fertile_sector_array((N - 1) - 1, (A[- N][- N] + A[- N][- N + 1]), (A[- N + 1][- N] + A[- N + 1][- N + 1]), accumulator)
            except:
                pass

    fertile_sector_array(N, A[- N][- N] + A[- N][- N + 1], A[- N + 1][- N]+ A[- N + 1][- N + 1], 0)
    
    # pass

def test2(N, A):
    pass

def main():
    # 3 by 3 array
    N = 3
    A = [[1, 3, 5], [4, 8, 2], [7, 9, 6]]
    print(test1(N, A))
    
    pass

if __name__ == '__main__':
    main()