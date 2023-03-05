# python3

import readline
import sys
import threading
import numpy as cc  
def compute_height(n, parent):
    limeni{}
    maxgar = 0
    for j in range(n):
        garums = 0
        z=j
        while z!=-1:
            if z in limeni:
                garums += limeni[z]
                break
            garums +=1
             
            z=parent[z]
        z = j
        while z != -1:
            if z in limeni:
                garums += limeni[z]
                break
            limeni[z] = garums
            garums -=1
            z = parent[z]
        maxgar = max(maxgar, limeni[j])
    return maxgar

        

def main():
   
    text = input("Ievadat: ")
    if "I" in text:
        n = int(input().strip())

        parent = cc.array(list(map(int,input().split())))
    elif "F" in text:
        fileName = str(input())
        if "a" in fileName:
            print("fails satur a")
        try:
            fileName="test/" + str(fileName)
            with open(fileName,'r', encoding="utf8") as jaunsf:
                 n = int(jaunsf.readline().strip())
                 parent =cc.array(list(map(int, jaunsf.readline().split())))
        except FileNotFoundError:
            print("fails nav atrasts")
            return
    
    
    atrisinajums = compute_height(n,parent)
    print(atrisinajums)

    
    
    
    
if __name__ == "__main__":    
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()

    

