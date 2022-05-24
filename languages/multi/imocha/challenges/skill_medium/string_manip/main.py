def subStrings(A,B):
    
    # approach 1: find and work with how many duplicate substrings occur in list A
    def test1(A, B):
        combined_list = []
        count = 0
        res = {}
    
        for i in A:
            for j in B:
                if (j == i):
                    combined_list.append(i)

        for k in combined_list:
            for l in B:
                if (k == l):
                    count += 1
        
        for m in combined_list:
            res[m] = combined_list.count(m)

        max_count_duplicates = res[f'{max(res)}']

        return max_count_duplicates

    
    # def test2(A, B):
    #     match B:
    #         case []:


    
    result = test1(A, B)

    # DEBUG: show raw output
    # result= A, B
    
    return result

#INPUT [uncomment & modify if required]
A=str(input())
B=str(input())

#OUTPUT [uncomment & modify if required]
print(subStrings(A,B))