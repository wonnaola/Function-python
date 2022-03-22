def num():
    user=int(input("enter the number"))
    i=1
    b=0
    while i<=user:
        if i%1==0 and user%user==0:
            b+=1
        i+=1
    if b==2:
        print("prime number")
    else:
        print("not prime number")    
num()
