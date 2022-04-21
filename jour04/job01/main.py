def puissance(x, n):
    if n == 0:
        return 1
    else:
        return x*puissance(x, n-1)

x = int(input("Entrez un entier : "))
n = int(input("Puissance : "))

if x == 0: 
    print(x,"^",n,"=",x)

elif n == 1:
    print(x,"^",n,"=",x)

else: 
    print(x,"^",n,"=",puissance(x, n))


