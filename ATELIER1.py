#exercice 1

def fact(n):#fact() est une fonction qui permet de calculer le factoriel
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
n=int(input("entrer une valeur:"))# demande a l'utulisateur de saisir une valeur
print("le factoriel de",n,"est",fact(n)) #affichage du factorielle d'un nombre donne
sum=0
for i in range(1,n):
    sum=sum+fact(n)/n
print("la somme de la serie :",sum) #affichage de la somme

#exercice 2

a=int(input("entrer un nombre ")) #le nombre a convertir
b=0 #l'equivalent de a en binaire
ord=0
while a!=0 :#repeter les instructions  jusqu'a a=0
    reste=a%2 #le reste de la division de a par 2
    p=10**ord
    b=b+reste*p
    ord=ord+1 #incrementation de la valeur de l'ordre
    a=a//2 #l'affectation du resultat de la division entiere
    print(b)

#exercice 3

s = 0
n = int(input("entrer la valeur de n"))
for i in range (0,n+1) :
    s = s+i
print("la somme 1+2+....+n:","est:" ,s)

#exercice 4

def fibonacci (n):
    if(n<=1): #fin de recursivite
        return 1 # la fibonacci de 1 est 1
    else :
        return (fibonacci(n-1)+fibonacci(n-2)) #affiche la fibonacci du nombre de termes entree
n=int(input("entrer le nombre de termes:"))
for i in range(n) :
    print(fibonacci(i)) #appel de la fonction recursive

#exercice 5

def Chiffre(n):
        if (n< 10) : # fin du recursivite
            return 1 # retourne 1 si le nombre est inferieur à 10
        else :
            return 1 + Chiffre(n/10); #il retoune le resultas du nombre diviser par
                                      # 10 jusqu'à le nombre devient indivisible par 10
n=int(input("entrer un Chiffre:")) #demande à l'utilisateur d'entrer un chiffre
print(Chiffre(n)) #affiche le nombre de chiffre


#exercice 7

ch1=input("entrer une chaine:")
ch2=""
i = len(ch1) - 1 #index du dernier caractere de ch1
while i >= 0:
    ch2 += ch1[i] #on ajoute un caractere de ch1 en partant de la fin a ch2
    i -= 1
print(ch2)

#exercice 8

def frequence(ch):
    nbr=ch.count(n) #il va calculer le nombre d'occurence du caractere dans la chaine
    return nbr #il va retourner le nombre d'occurence
ch=str(input("entrer une chaine de caractere:")) #demaande à l'utilisateur d'entrer une chaine
n=str(input("entrer le caractere n:"))
print(frequence(ch)) # appel la fonction recursive

#exercice 9

def cherche(l):
    for i in l:
        x=0
        for j in i :
            if j==k:
               print("i=",l.index(i),"j=",x)
            x=x+1
l=[[8,10,7],
       [5,6,1],
       [3,6,4]]
k=int(input("saisir la valeur chercher"))
print(cherche(l))












