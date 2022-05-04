def newString(S):
    t = S

    S_alpha = sorted(S, reverse=True)

    for i in S_alpha:
        if i in S_alpha: del i

    return S_alpha

def main():
    S = "ababc"

    print(newString(S))

if __name__ == '__main__':
    main()