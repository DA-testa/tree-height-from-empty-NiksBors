# python3

import readline
import sys
import threading
import numpy  
def compute_height(n, parent):
    garums = numpy.zeros(n)

    maxgar = -1
    for j in range (len(parent)):
        z = j
        limeni = 1
        while parent[z] != -1:
            if limeni[z] !=0:
                limeni += limeni[z]-1
                return
            
            limeni +=1
            z=parent[z]
            limeni[j] = limeni
            maxgar = max(maxgar, limeni[j])
        return maxgar
    

  



   
  

def main():
    text = input("Ievadat:")
    if "F" in text:
        fileName = input()
        
        if ".a" in fileName:
            return
        if ".a" not in fileName:
            jaunsf = "test/"+fileName
            with open(jaunsf, 'o') as jap:
                n = int(jap,readline())
            tree = compute_height(n,parent)
            print(tree)
    elif "I" in text:
        n = input()
        parent = list(map(input().split()))

    
    
    
    
    
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
