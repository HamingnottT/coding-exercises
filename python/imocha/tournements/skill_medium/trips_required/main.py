import math

# def trips_required(N, K, A):

#     max_from_list = max(A)

#     result = max_from_list

#     return result


def trips_required(N, K, A):
    city_list = []
    carry_at_a_time = []
    sum_of_people = sum(A)

    for i in range(1, N + 1):
        city_list.append(i)

    for j in range(1, K + 1):
        carry_at_a_time.append(j)

    return city_list, carry_at_a_time, sum_of_people / K


def tripsRequired(N,K,A):

    city_list = []
    carry_at_a_time = []
    sum_of_people = sum(A)

    for i in range(1, N + 1):
        city_list.append(i)

    for j in range(1, K + 1):
        carry_at_a_time.append(j)

    test1 = city_list, carry_at_a_time
    
    test2 = math.ceil(sum_of_people / K)

    
    result = test2

    return result

#INPUT [uncomment & modify if required]
N=int(input())
K=int(input())
A=[]

for i in range(N):
    A.append(int(input()))
    
#OUTPUT [uncomment & modify if requi

def main():
    N = 5
    K = 3
    A = [1, 2, 1, 0, 0]
    
    
    print(trips_required(N, K, A))


if __name__ == '__main__':
    main()