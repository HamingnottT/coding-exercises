import re


def cubeSquare(T, N):
    def sq_root(number):
        return number ** (1/2)

    def cube_root(number):
        return number ** (1/3)  

    N_to_string = []
    boolean_checker = []
    cube_list = []
    
    for i in N:
        N_to_string.append()

    for item in N:
        for number in item:
            print(number)


    # # debug
    # return T, N

def main():
    T = 3
    N = [10, 25, 1]

    for i in N:
        print(cubeSquare(T, i))

if __name__ == '__main__':
    main()