def prime_range(lw,up):
    for num in range(lw,up+1):
        count=0
        for dig in range(1,num//2+1):
            if num%dig==0:
                count+=1
        if count==1:
            print(num,end=" ")
            
prime_range(1,100)
