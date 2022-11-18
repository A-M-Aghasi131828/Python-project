def EX3_5(l):
    z=0
    for i in l:
        if i < 0:
            i = -1 * i
        z=z+i
    if z == 25:
        return True
    else:
        return False
