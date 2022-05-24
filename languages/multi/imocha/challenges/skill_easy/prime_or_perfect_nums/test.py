def primeOrPerfectSquareDivisors(N):
    
    # attempt 1:
    def test1(N):
        
        # stack overflow returned with large numbers - revise
        def get_factors(factor, N, accum):
            if factor == 0: return accum
            else:
                if (N % factor == 0): accum.append(factor)
                return get_factors(factor - 1, N, accum)

        
        def is_prime(N):
            def is_prime_until(t):
                if t <= 1: return True
                else: return N % t != 0 and is_prime_until(t - 1)
            return is_prime_until(N / 2)

        
        factors_list = get_factors(factor=N, N=N, accum=[])
        is_prime_list = []
        perfect_square = []

        for i in factors_list:
            if is_prime(i) == True: is_prime_list.append(i)

        for j in is_prime_list:
            if i / i == 1:
                perfect_square.append(j)
        
        return perfect_square[0]


    return test1(N)


# INPUT [uncomment & modify if required]
N = int(input())

# OUTPUT [uncomment & modify if required]
print(primeOrPerfectSquareDivisors(N))