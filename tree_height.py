# python3

import readline
import sys
import threading
import numpy as cc  
def compute_height(n, parent):
    garums = cc.zeros(n)

    maxgar = -1
    for j in range (len(parent)):
        z = j
        limeni = 1
        while parent[z] != -1:
        
            
            limeni +=1
            z=parent[z]
        garums[j] = limeni
        maxgar = max(maxgar, garums[j])
     return maxgar
    

  



   
  

def main():
    text = input("Ievadat:")
    if "F" in text:
        fileName = input()
        file='./test/'+fileName
        if "a" not in fileName:
            try:
                with open(file) as jaunsf:
            c = int(jaunsf.readline())
            parent = list(map(int, jaunsf.readline().split()))
           except FileNotFoundError:
            print("fails nav atrasts")
            return
        else:
            parent = []
    elif "I" in text:
        n = int(input())
        parent = list(map(int,input().split()))

    
    
    
    
    
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start(), args=(n, parent)).start()
if_name == "__main__":
    main()

