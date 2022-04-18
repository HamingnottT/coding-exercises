def calcSteps(S):
    
    # using time complexity to solve
    def minCut(S):
        cut = [0 for i in range(len(S))]
        palindrome = [[False for i in range(len(S))] for j in range(len(S))]
        for i in range(len(S)):
            minCut = i
            for j in range(i + 1):
                if (S[i] == S[j] and (i - j < 2 or palindrome[j + 1][i - 1])):
                    palindrome[j][i] = True
                    minCut = min(minCut,0 if  j == 0 else (cut[j - 1] + 1))
            cut[i] = minCut
        return S[cut[len(S) - 1]]
    
    print(minCut(S))
    
    def findPal(S):
        
        return

    print(findPal(S))

    result=-404
    #write your Logic here:
    
    return result

#INPUT [uncomment & modify if required]
# S=input()
S = 'abcbh'

#OUTPUT [uncomment & modify if required]
print(calcSteps(S))