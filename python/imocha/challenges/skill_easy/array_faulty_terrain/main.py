from ssl import ALERT_DESCRIPTION_ACCESS_DENIED


def removeCoach(N, K, A):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','q','R','S','T','U','V','W','X','Y','Z']
    A_dict = {}

    def getList(dict):
        return list(dict.keys())

    for i in range(0, len(A)):
        A_dict[alphabet[i]] = A[i]

    for i in range(0, len(A)):
        if A[i] < K: del A_dict[alphabet[i]]
    
    result = " ".join([str(value) for value in getList(A_dict)])

    return result

def main():
    N = 3
    K = 100
    A = [400, 300, 10]

    print(removeCoach(N, K, A))

if __name__ == '__main__':
    main()