#even or odd
def even(n):
    if n%2==0:
        return "even"
    else:
        return "odd" 
    

#l=[23,45,78,67,78,67]
def unique(l):
    li=[] #23,45
    for i in l: #23,45,78,67
        if l.count(i)==1:
            li.append(i)
    print(li)
        