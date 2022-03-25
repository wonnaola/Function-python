def num(x):
    i=0
    j=1
    sum=0
    sum1=0
    while i<len(x):
        sum+=x[i]
        sum1+=x[j]
        j+=2
        i+=2
    print("sum=",sum)
    print("sum1=",sum1)
num([5,4,0,1,9,7])
        
    