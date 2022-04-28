# Objective: take a string, split it, and return it in revered order

def lexicographicDeccreasing(S):
    
    # using sorted(S, reverse=True) or S.sort(reverse=True) works
    s_reversed = sorted(S, reverse=True)

    # output of s_reversed is a reverse-order list, i need to turn it into a string

    # need container for the string that will be created
    s_to_string = ""

    # iterates over every index value in s_reversed then increments the value to the container s_to_string
    # is the same thing as 'for i in range(x, y)'
    for i in s_reversed:
        s_to_string += i

    # assigns the newly made string into the result variable
    result= s_to_string
    
    # prints the result to the console
    print(result)

#INPUT
temp = input().split()
# temp = "oklahoma".split()

S = temp[0]

#OUTPUT
lexicographicDeccreasing(S)
