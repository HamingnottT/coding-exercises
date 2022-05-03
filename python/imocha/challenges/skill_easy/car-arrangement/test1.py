# New attempt from challenge 5/23

def carArrangement(N, A):
    
    # partial correct from before but baseline for this attempt
    # the result was printed backwards
    def test1(N, A):
        mod_res = ""
        mod_counter_0 = 0
        mod_counter_1 = 0

        try:
            for A[i] in A:
                if(A[i] % 2 == 0):
                    mod_counter_0 += 1
            
            for A[i] in range(0, len(A)):
                if(A[i] % 2 == 0):
                    mod_counter_1 += 1

        except ZeroDivisionError:
            mod_counter_0 += 1
        finally:
            pass
        
        preresult = f"{round(mod_counter_0/2)} {abs(mod_counter_1)}"

        return preresult


    result = test1(N, A)

    return result


# INPUT [uncomment & modify if required]

N = int(input())

temp = input().split()
A = []
for i in range(N):
    A.append(int(temp[i]))

# OUTPUT [uncomment & modify if required]
print(carArrangement(N,A))