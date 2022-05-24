def bkg(N, K, A):
    A_sort_desc = sorted(A, reverse=True)

    del A_sort_desc[K]

    print(sum(A_sort_desc))

def main():
    N = int(input("N = "))
    K = int(input("K = "))
    A = []
    temp = input("A = ")
    temp = temp.split(" ")
    for i in temp:
        A.append(int(i))

    bkg(N, K, A)

if __name__ == '__main__':
    main()