import math

def painters(t, n):
    
    cube = 0
    watercolor = cube * 2
    poster = math.floor(cube * 0.5)

    per_int = 0

    def cube_scale(cube_size):
        if (cube_size > 0):
            watercolor
            poster
            
        else:
            watercolor = cube * 2
            poster = math.floor(cube * 0.5)

    for int in n:
        for l in range(0, int):
            cube += l
            per_int += watercolor + poster

    return print(per_int)

t = 2
n = [14, 15]
painters(t, n)