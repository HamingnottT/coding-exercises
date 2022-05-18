import re

def sq_root(number):
        return number ** (1/2)

def cube_root(number):
    return number ** (1/3) 


print(re.search(str(sq_root(9)), ".0"))
print(re.search(str(cube_root(9)), ".0"))

re.search(str(sq_root(9)), ".0")

x = str(sq_root(9))

for i in range(0, len(x)):
    try:
        if str(x[i]+x[i+1]) == ".0":
            print("yes")
        else: print("no")
    except:
        pass
