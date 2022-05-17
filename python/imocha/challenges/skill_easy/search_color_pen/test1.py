from operator import index


def colorPen(N, Q, A, queries):
    
    list_start = []
    query_start = []

    for i in A:
        list_start.append(str(i))
    for j in queries:
        query_start.append(str(j))

    for i in query_start:
        for j in list_start:
            if j == i:
                print(list_start.index(i) + 1)


    result = ""
    return result

def main():
    N, Q = 7, 5
    A = [2, 1, 1, 4, 3, 3, 1]
    queries = [3, 2, 1, 1, 4]

    print(colorPen(N, Q, A, queries))

if __name__ == '__main__':
    main()