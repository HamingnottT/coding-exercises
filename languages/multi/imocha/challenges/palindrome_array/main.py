from itertools import permutations
import string

def lexicographical_order():
    test_list = [[1, 4, 3, 2], [5, 4, 1], [1, 4, 6, 7]]
    
    # printing the original list
    print ("The original list is : " + str(test_list))
    
    # using sort() twice 
    # sort list of lists by value and length
    test_list.sort()

    print ("The list after sorting by value and length " + str(test_list))


def palindrome_array():
    def lexicographical_permutation(str):
        list = []
        perm = sorted(''.join(chars) for chars in permutations(str))
        
        # print(perm)
        # for x in perm:
        #     print(x)

        str_2_int = int(str)

        for char in str:
            list.append(char)

        for char in list:
            int_list = int(char)

        print(int_list)
            
    str ='11232'
    lexicographical_permutation(str)

palindrome_array()

def findPalindrome(N, A):
    # this is default OUTPUT. You can change it.
    # perm = sorted(''.join(chars) for chars in permutations(A))
    
    perm = permutations(A)

    test_list = []

    for i in list(perm):
        test_list.append(i)

    
    result = test_list

    # write your Logic here:
    
    
    return result


# INPUT [uncomment & modify if required]

N = 5 #int(input())
temp = '1 1 2 3 2'.split() #input().split()
A = []
for i in range(N):
    A.append(int(temp[i]))

# OUTPUT [uncomment & modify if required]
print(findPalindrome(N, A))