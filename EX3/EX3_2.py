def EX3_2(n):
    z = []
    
    for i in range(0 , len(n)-1):
        y = n[i] * n[i+1]
        z.append(y)
    z.sort(reverse=True)
    return z[0]
