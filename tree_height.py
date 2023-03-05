# python3

import readline
import sys
import threading
import numpy as cc  
def compute_height(n, parent):
    garums = cc.zeros(n, dtype=int)
    def papildfunk(mezgls):
        stack = [(mezgls,0)]
        while stack:
            mezgls, limeni = stack.pop()
            garums[mezgls]=limeni
            for b in cc.where(parent == mezgls)[0]:
                 stack.append((b, limeni+1))
    for mezgls in range(n):
        if garums[mezgls] == 0:
            papildfunk(mezgls)
    return cc.max(garums)
    
        

def main():
   
    text = input("Ievadat: ")
    if "I" in text:
        try:
            n = int(input().strip())
        except ValueError:
            return
        parent = cc.array(list(map(int,input().split())))
    elif "F" in text:
        fileName = str(input())
        if "a" not in fileName:
            try:
                file='./test/' + fileName
                with open(file,'r') as jaunsf:
                    c = int(jaunsf.readline())
                    parent =cc.array(list(map(int, jaunsf.readline().split())))
            except FileNotFoundError:
                print("fails nav atrasts")
                return
        else:
            print("error")
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

    

