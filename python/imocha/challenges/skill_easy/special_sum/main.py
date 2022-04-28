def SpecialSum(N, Arr, K):
    
    def split_list_from_string(string):
        string_list = string.split(" ")
        return string_list
    
    list = split_list_from_string(Arr)

    def list_string_2_int(list):
        new_list = []
        for i in range(0, len(list)):
            new_list.append(int(list[i]))
        return new_list

    int_list = list_string_2_int(list)

    first_n = int_list[:(K)]

    del int_list[(K):(K+K)]

    sum(int_list)

    
    # for debugging
    print(first_n)
    print(sum(int_list))
    pass

def main():
    # N = 14
    # Arr = "1 5 9 7 8 6 4 3 2 1 0 5 8 7"
    # K = 5

    N = 13
    Arr = "27 49 27 36 11 40 33 33 47 17 2 23 31"
    K = 4

    SpecialSum(N, Arr, K)

if __name__ == '__main__':
    main()