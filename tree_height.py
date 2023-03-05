# python3

import readline
import sys
import threading
import numpy as cc  
def compute_height(n, parent):
    limeni = {} # izveido jaunu vārdnīcu/ objektu
    maxgar = 0 # pievienoju visgarāko mezglu, un pielīdzinu nullei
    for j in range(n): # izveido ciklu, lai izietu cauri katram koka mezglam, un seko cauri katram punktam līdz tiek pie vecāka, jeb -1
        garums = 0
        z=j
        while z!=-1: # kamēr nav sasniegts vecāks, liek koka garumam klāt 1nieku.
            if z in limeni:
                garums += limeni[z]
                break
            garums +=1
             
            z=parent[z]
        z = j # tagad pāŗbauda vai virs mezgliem nav vēl koka daļas, ja ir jau sasniegts -1, tad iziet no cikla, taču, ja saprot, ka ir aprēķinātst tikai subtree, tad palielina garumu
        while z != -1:
            if z in limeni:
                garums += limeni[z]
                break
            limeni[z] = garums
            garums -=1
            z = parent[z]
        maxgar = max(maxgar, limeni[j])
    return maxgar

        

def main(): # funkcija apstrādās I un F ievadi, sākumā pārbaudot, vai lietotājs ir ievadījis I, ja ir ievadījis, tad sāk nolasīt mezglu un vecāku msaīvu skaitu
   
    text = input("Ievadat: ")
    if "I" in text:
        n = int(input())

        parent = cc.array(list(map(int,input().split())))
    elif "F" in text: # ja lietotājs ir ievadījis F, tad nolasa mezglu daudzumu un vecāku masīvu no faila, pēcāk pāŗbauda vai faila nosaukumā nav a burts
        fileName = str(input())
        if "a" in fileName:
            print("fails satur a")
        try:
            fileName="test/" + str(fileName)
            with open(fileName,'r') as jaunsf:
                 n = int(jaunsf.readline())
                 parent =cc.array(list(map(int, jaunsf.readline().split())))
        except FileNotFoundError:
            print("fails nav atrasts")
            return
    
    
     # šeit izprintē
    print( compute_height(n,parent))

    
    
    
    
if __name__ == "__main__":    
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()

    

