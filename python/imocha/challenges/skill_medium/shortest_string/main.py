from cgi import test


def test1(N, S):
    S_to_list = []
    for char in S:
        S_to_list.append(char)

    try:
        for char in range(0, len(S_to_list) - 1):
            if (S_to_list[char-1]+S_to_list[char] == "01"):
                del S_to_list[char - 1]
                del S_to_list[char]
            
        for char in range(0, len(S_to_list) - 1):    
            if (S_to_list[char-1]+S_to_list[char] == "11"):
                del S_to_list[char - 1]
                del S_to_list[char]
    except:
        pass # rough termination if there is IndexOutOfBounds exeception
    
    return len(S_to_list)
            
    
    # ~ debug ~
    # return N, S



def main():
    N = 4
    S = "1011"
    print(test1(N=N, S=S))


if __name__ == '__main__':
    main()