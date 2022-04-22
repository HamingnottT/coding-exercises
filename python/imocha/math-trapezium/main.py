def test1(px, qx, rx):
    tx = (px + qx + rx)/4

    result = "{:0.2f}".format(tx)

    return result

def main():
    px, qx, rx = int(input("px = ")), int(input("qx = ")), int(input("rx = "))

    print(test1(px, qx, rx))

if __name__ == '__main__':
    main()


# original answer

# def areaOfTrapezium(px,qx,rx):
    
#     tx = (px + qx + rx)/4

#     result = tx
    
#     print("{:.2f}".format(result))

# #INPUT [uncomment & modify if required]
# temp=input().split()

# px=int(temp[0])
# qx=int(temp[1])
# rx=int(temp[2])
# #OUTPUT [uncomment & modify if required]
# areaOfTrapezium(px,qx,rx)