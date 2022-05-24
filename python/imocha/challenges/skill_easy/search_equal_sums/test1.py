def equalSums(S):

    s = S.lower()



    alphabet = "abcdefghijklmnopqrstuvwxyz"

    alpha_counter = 1

    alpha_dict = {}



    for i in alphabet:

        alpha_dict[i] = alpha_counter

        alpha_counter += 1

    

    S_first_half = S[:int(len(S)/2)].lower()

    S_last_half = S[int(len(S)/2):].lower()

    S_first_half_sum = 0

    S_last_half_sum_p1 = 0



    alpha_dict_keys = list(alpha_dict.keys())

    alpha_dict_values = list(alpha_dict.values())



    for j in S_first_half:

        S_first_half_sum += alpha_dict[j]

    

    while(S_last_half_sum_p1 != S_first_half_sum):

        for k in S_last_half:

            S_last_half_sum_p1 = alpha_dict[k]

    

    

    

    # result = alpha_dict_key[S_last_half_sum_p1]
    result = ""


    return result





# INPUT [uncomment & modify if required]

S = input()



# OUTPUT [uncomment & modify if required]

print(equalSums(S))