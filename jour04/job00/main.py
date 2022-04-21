def factorielle(n):
    if n == 1:
        return n
    else: 
        return n*factorielle(n-1)

n = int(input("Entrez un nombre entier : "))

if n < 0: 
    print("La factorielle d'un nombre négatif ne peut etre trouver")

elif n == 0: 
    print("La factorielle de 0 est 1")

else: 
    print("La factorielle de",n, "est :",factorielle(n))
