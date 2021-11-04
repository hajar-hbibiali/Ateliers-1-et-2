l1=[3,6,9,12,15,18,21,2]
l2=[4,8,12,16,20,24,28]

#quest1
li= []
count = 0
for i in l1: #boucle pour extraire les elements d'indice impaire da la liste 1
    if count % 2 == 1:
        li.append(i)#si l'indice est impaire on ajoute l'element  à la nouvelle liste li
    count += 1 #incrimmentation du count
count=0
for i in l2 :#boucle pour extraire les elements d'indice paire da la liste 2
    if count % 2 ==0:
        li.append(i) #si l'indice est paire on ajoute l'element  à la nouvelle liste li
    count +=1
"""il va afficher la nouvelle liste li qui contion les elements d'indice impair de l1
 et les elememts d'indice paire de l2"""
#print(li)

#quest2


L=[7,5,2,6,8,4]
x=len(L)//3 #diviser la liste en 3 morceaux
y=2*len(L)//3
nvl1=L[:x]
nvl2=L[x:y]
nvl3=L[y:]
print( nvl1[::-1],nvl2[::-1],nvl3[::-1]) #inverser les 3 morceaux puis l'afficher

#quest3

my_list=[12,65,8,23,12,5,5]
d={}
for i in my_list:
    if my_list.count(i)>1:# extraire les elements qui se repete plusieurs fois
        d.update({i:my_list.count(i)})
        del(i) #supprimer l'element trouver
    else :
        d.update({i:my_list.count(i)}) # ajouter l'element dans le dictionnaire
print(d,end="")

#quest4"

set1={25,65,89,54,77,5}
set2={55,89,66,76,55,33}
set=set1.intersection(set2)#faire l'intersection entre les deux sets et afficher le resultas
print ("intersection de deux sets est:",set)
#trouver la difference entre les 2 sets et afficher les resultas
print("le set1 apres la supression est :",set1.difference(set))

#quest 5

list1 =[55,23,24,79,66,89,54,67]
dict1={'hajar':55,'asemae':24,'mohamed':66,'abir':67}
keys= list(dict1.keys())
result=[]
for i in keys:
    for j in list1:#boucle pour parcourir la liste
        if dict1[str(i)]==j:result.append(j)#ajouter les elements j au dict1
print(result)#affiche le resultat final






