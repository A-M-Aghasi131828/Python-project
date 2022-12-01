'''
Amir Mahdi Aghasi
4012061005
'''
W=['A','B','C','D','E','F','G','H','a','b','c','d','e','f','g','h']
N=['1','2','3','4','5','6','7','8','1','2','3','4','5','6','7','8']
WB=input('Please enter horizontal position of the bishop (A,B,C,D,E,F,G,H,a,b,c,d,e,f,g,h): ')
if WB.isalpha()==False:
    print ('Horizontal input for bishop is not a letter')
elif WB.isalpha()==True and WB not in W:
    print ('Horizontal input for bishop is not a proper letter')
else:
    NB=input('Please enter vertical position of the bishop (1,2,3,4,5,6,7,8): ')
    if NB.isnumeric()==False:
        print ('Vertical input for bishop is not a number')
    elif NB.isnumeric()==True and NB not in N:
        print ('Vertical input for bishop is not a proper number')
    else:
        WK=input('Please enter horizontal position of the knight (A,B,C,D,E,F,G,H,a,b,c,d,e,f,g,h): ')
        if WK.isalpha()==False:
            print ('Horizontal input for knight is not a letter')
        elif WK.isalpha()==True and WK not in W:
            print ('Horizontal input for knight is not a proper letter')
        else:
            NK=input('Please enter vertical position of the knight (1,2,3,4,5,6,7,8): ')
            S1=W.index(WB)
            S2=W.index(WK)
            S3=N.index(NB)
            S4=N.index(NK)
            S1+=1
            S2+=1
            S3+=1
            S4+=1
            if S1 > 8 :
                S1-= 8
            if S2 > 8:
                S2-= 8
            if S3 > 8 :
                S3-= 8
            if S4 > 8:
                S4-= 8
            if NK.isnumeric()==False:
                print ('Vertical input for knight is not a number')
            elif NK.isnumeric()==True and NK not in N:
                print ('Vertical input for knight is not a proper number')
            else:
                '''
                the program to vheck if bishop and knight are in the same place
                '''
                while S2==S1 and S4==S3 :
                    print ("They can't be in the same square")
                    break
                '''
                the program to check if bishop can attack knight
                '''
                H=S2-S1
                if H < 0 :
                    H = H * -1
                V=S4-S3
                if V < 0 :
                    V = V * -1
                if H==V:
                    print ('Bishop can attack knight')
                else:
                    '''
                    the program to check if knight can attack bishop
                    '''
                    HH=S2-S1
                    if HH < 0 :
                        HH *= -1
                    VV=S4-S3
                    if VV < 0 :
                        VV *= -1
                    if VV == 1 and HH == 2:
                        print ('Knight can attack bishop')
                    elif VV == 2 and HH == 1:
                        print ('Knight can attack bishop')
                    else:
                        print ('Neither of them can attack each other')
