def Comma_Code(x):
    y=''
    for items in range(len(x) -1):
        y += str(x[items])+', '
    z= 'and ' + str(x[-1])
    return (y+z)
    
l = [1,2,3,4,5,6,7,8,9,0]
print (Comma_Code(l))