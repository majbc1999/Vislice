#Program za prvih 200 praštevil

def prastevila(stevila):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for x in range(2,201):
    if prastevila(x):
        print(x)
    
    