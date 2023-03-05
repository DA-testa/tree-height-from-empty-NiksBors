# python3

import readline
import sys
import threading
import numpy  
def compute_height(n, parent):
    adj_list = [[]for _ in range(n)]
    for j, v in enumerate(parents):

        if  v!=-1:
            adj_list[v].append(i)
    
    stack =[(parents.index(-1),1)]
    max_height =0
    while stack:
        l, garums = stack.pop()
        max_height = max(max_height, garums)
        for q in adj_list[v]:
            stack.append((q height +1))
    

    return max_height



   
  t

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
