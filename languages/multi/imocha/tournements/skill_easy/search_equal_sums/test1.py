def equalSums(S):
    s = S.lower()
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_counter = 1
    alpha_dict = {}       # "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "": 1, "": 1
    

    for i in alphabet:
        alpha_dict[i] = alpha_counter
        alpha_counter += 1

    # S_reversed = reversed(S.split(""))
    S_first_half = S[0:int(len(S)/2)].lower()
    S_last_half = S[int(len(S)/2):]   #S_reversed[0:int(len(S)/2)].lower()
    S_first_half_sum = 0
    S_last_half_sum_p1 = 0
    S_last_half_sum_p2 = 0

    alpha_dict_values = list(alpha_dict.values())

    for j in S_first_half:
        S_first_half_sum += alpha_dict[j]

    # pass one
    while(S_last_half_sum_p1 !=  S_first_half_sum):
        for k in S_last_half:
            S_last_half_sum_p1 = alpha_dict[k]



    return alpha_dict[S_last_half_sum_p1]

def main():
    S = "abec"
    print(equalSums(S))

if __name__ == '__main__':
    main()