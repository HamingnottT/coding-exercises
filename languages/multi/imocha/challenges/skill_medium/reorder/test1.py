def reorder(N, arr):
    pair_arr = []
    pair_arr_index = []

    # for i in range(0, len(arr)):
    #     print(i)

    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if (N >= j > i >= 1):
                pair_arr.append((arr[i], 2*arr[j]))
                pair_arr_index.append((i, j))

    # for i in arr:
    #     for j in arr:
    #         pair_arr.append((arr.index(i), arr.index(j)))


    result = len(sorted(pair_arr_index))

    return result

def main():
    N = 5

    arr = [1, 4, 2, 4, 1]

    print(reorder(N, arr))

if __name__ == '__main__':
    main()