def nearestMultiple(N):
    #this is default OUTPUT. You can change it.
    #write your Logic here:

    # divide whole number N by 100 or multiply by 0.01
    # then round to the nearest tenth

    n_round_tenth = round(N*0.01, 1)

    # take the result of the previous method and multiply 100 to return to whole number form
    n_result = round(n_round_tenth*100)

    result = n_result

    return result



#INPUT [uncomment & modify if required]

N = int(input())

#OUTPUT [uncomment & modify if required]

print(nearestMultiple(N))