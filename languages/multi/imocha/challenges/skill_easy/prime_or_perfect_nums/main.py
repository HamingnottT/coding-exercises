import os
import math

def test1(N):
    
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
    

    factors_list = get_factors(N, N, [])
    is_prime_var = []
    perfect_square = []

    for i in factors_list:
        if is_prime(i) == True: is_prime_var.append(i)

    for i in is_prime_var:
        if i / i == 1:
            perfect_square.append(i)

    return factors_list, is_prime_var, perfect_square[0]
    

def main():
    N = 10
    print(test1(N))


if __name__ == '__main__':
    os.system("py -3 --version") # for py -3 -m main command
    main()