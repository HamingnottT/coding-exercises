def sq_root(number):
        return number ** (1/2)

def cube_root(number):
    return number ** (1/3) 

def getSquareList(numInput, accum):
        if (numInput == 0): return accum
        else: return getSquareList(numInput - 1, accum.append(sq_root(numInput)))

getSquareList(10, [])