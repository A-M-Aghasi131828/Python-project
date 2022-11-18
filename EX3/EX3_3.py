def EX3_3(n):
    '''
    Destination No. 1: e, n, e, e, n --> 3e and 2n
    Destination No. 2: w, n, w, n, w, w, n --> 4w and 3n
    '''
    a = n.count("e")
    b = n.count("w")
    c = n.count("n")
    d = n.count("s")
    if a-b == 3 and c-d == 2:
        return(True)
        
    else:
        if b-a == 4 and c-d == 3:
            return(True)
        else:
            return(False)
