import random as rd

liste_Candidats={0:"Candidat A",1:"Candidat B", 2:"Candidat C", 3:"Candidat D"}

## Duel entre le candidat n° i et celui n°j. Résultat positif sur i gagne et negatif sur j gagne. le résultat est le nombre de vote de plus pour i (ou de moins).
def duel(votes,i,j):
    res=0
    for k in votes:
        p=0
        while k[p]!=i and k[p]!=j:
            p+=1
        if k[p]==i:res+=1
        else: res-=1
    return(res)

def matrice_duels(votes):
    nb=len(votes[0])
    matrice=[[0 for j in range(nb)] for i in range(nb)]
    for i in range(nb):
        for j in range(nb):
            if i!=j:
                matrice[i][j]=duel(votes,i,j)
            else:
                matrice[i][j]=0
    return(matrice)
def est_vainqueur(liste,i):
    res=True
    nb=len(liste)
    j=0
    while j<nb and res:
        if i!=j:res = liste[j] > 0
        j+=1
    return(res)

def vainqueur_de_condorcet(votes):
    mat=matrice_duels(votes)
    vainq=False
    nb=len(mat)
    i=0
    while i<nb and not vainq:
        vainq=est_vainqueur(mat[i],i)
        i+=1
    if vainq:return(i-1)
    else:raise ValueError ("Pas de Vainqueur")
        
        
def nombre_duel_gagne(votes):
    mat=matrice_duels(votes)
    nb=len(mat)
    res=[0 for i in range(nb)]
    for i in range(nb):
        for j in range(nb):
            if i!=j:
                if mat[i][j]>0:
                    res[i]+=1
                elif mat[i][j]==0:
                    res[i]+=0.5
    return(res)

def recherche(liste,p):
    n=len(liste)
    a=0
    b=n-1
    if p < liste[0]:return(0)
    while b-a > 1:
        c= (b+a)//2
        if liste[c] > p:
            b=c
        else:
            a=c
    return(b)
        

def condorcet_rando(votes):
    nb=len(votes[0])
    nbd=nb*(nb-1)/2
    try:
        return(vainqueur_de_condorcet(votes))
    except:
        L=nombre_duel_gagne(votes)
        L[0]=L[0]/nbd
        for i in range(1,nb):
            L[i]=L[i-1] + L[i]/nbd
        p=rd.random()
        return(recherche(L,p))
            
        

liste_votes=[[0,2,1,3,4],[2,4,0,3,1],[4,2,0,1,3],[0,2,3,1,4],[1,0,2,3,4],[1,0,2,4,3],[1,2,3,4,0]]
votes2=[[0,1,2,3],[3,1,2,0],[2,0,3,1],[1,0,2,3],[1,2,0,3]]
res=[0,0,0,0]
for i in range(50000):
    p=condorcet_rando(votes2)
    res[p]+=1
print(res)

mat=matrice_duels(liste_votes)




#print(duel(liste_votes,1,2))