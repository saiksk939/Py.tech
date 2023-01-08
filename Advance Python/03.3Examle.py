#4!=4*3*2*1=24
#3!=3*2*1=6

def fact(x):
    if x==1:
        return 1
    else:
        return (x * fact(x-1))

print(fact(4))

