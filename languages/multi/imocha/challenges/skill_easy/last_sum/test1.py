# rough draft of main.py pre-submission

def last_sum(N, A):
    A_to_stringlist = []

    for i in A:
        A_to_stringlist.append(str(i))

    def last_sum_helper(N, A, Accum):
        if (N == 0): print(Accum)

        else:
            last_sum_helper(N - 1, A, int((A[N - 1])[-1]) + Accum)

    last_sum_helper(N, A_to_stringlist, 0)
    # print(A_to_stringlist)

def main():
    N = 3
    A = [123, 324, 2133]

    last_sum(N, A)

if __name__ == '__main__':
    main()