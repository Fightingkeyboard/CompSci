def Comma_Code(x):
    for items in range(len(x) -1):
        print (str(x[items])+', ', end ='')
    print ('and ' + str(x[-1]))
    
l = [1,2,3,4,5,6,7,8,9,0]
Comma_Code(l)