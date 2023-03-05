# python3

import readline
import sys
import threading
import numpy as cc  
def compute_height(n, parent):
    garums = cc.zeros(n)
    def papildfunk(mezgls):
        stack = [(mezgls,0)]
        while stack:
            mezgls, garums = stack.pop()

            garums[mezgls]=compute_height
        for b in cc.where(parent == mezgls)[0]:
            stack.append((b, garums+1))
    for mezgls in range(n):
        if garums[mezgls]==0:
            papildfunk(mezgls)
    return cc.max(garums)

    
    

  



   
  

def main():
    text = input("Ievadat:")
    if "F" in text:
        fileName = input()
        file='./test/' + fileName
        if "a" not in fileName:
            try:
                with open(file,'r') as jaunsf:
                    c = int(jaunsf.readline())
                    parent = list(map(int, jaunsf.readline().split()))
            except FileNotFoundError:
                print("fails nav atrasts")
                return
        else:
            print("error")
            return
    elif "I" in text:
        n = int(input())
        parent = list(map(int,input().split()))

    
    
    
    
if_name == "__main__":    
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start(), args=(n, parent)).start()

    

