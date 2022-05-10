def test1(N, X, K, M):
    can_afford = []
    cannot_afford = []
    can_afford_unique = []
    
    for i in M:
        for j in X:
            if (j <= i): 
                can_afford.append(j)
            else: 
                cannot_afford.append(j)

    for i in can_afford:
        if i not in can_afford_unique:
            can_afford_unique.append(i)

    return can_afford, cannot_afford, can_afford_unique

def test2(N, X, K, M):
    can_afford = []
    cannot_afford = []
    can_afford_dict = {}
    counter = 1
    result = ""

    for i in M:
        for j in X:
            if (j <= i): 
                can_afford.append(j)
                can_afford_dict[i] = counter
                counter += 1
            else: 
                cannot_afford.append(j)
        counter = 1

    result = " ".join([str(i) for i in can_afford_dict.values()])

    return result

def main():
    N = 5
    X = [3, 6, 8, 10, 11]
    K = 4
    M = [5, 10, 3, 11]
    
    print(test2(N, X, K, M))

if __name__ == '__main__':
    main()