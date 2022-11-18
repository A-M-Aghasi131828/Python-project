def EX3_1(n):
    m=0
    while n > 1:
        if n%2==0:
            n=n/2
            m=m+1
        elif (n-1)%2==0:
            n=(n*3)+1
            m=m+1
    if n == 1:
        return m
