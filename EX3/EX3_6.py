def EX3_6 (i):
    if len(i)==0:
        return (':/')
    i.sort()
    y = i[len(i)-1] - i[0]
    if i.count(y) == 1:
        return True
    else:
        return False
print(EX3_6([12,23,45,32,6,2,34,15]))