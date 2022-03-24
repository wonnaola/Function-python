def num(x):
    i=0
    j=1
    sum=0
    sum1=0
    while j<len(x):
        sum+=x[i]
        sum1+=x[j]
        i+=2
        j+=2
    
    print("sum=",sum+x[i])
    print("sum1=",sum1)
num([5,4,0,1,9])
        
    