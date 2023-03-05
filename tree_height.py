import sys
import threading
import numpy as np


def main():
  letter = input()
  if "I" in letter:
    count = int(input())
    main = list(map(int,input().split()))
    print(compute_height(count, main))
    
  elif "F" in letter:
    filename = input()
    if "a" not in filename:
      with open(str("test/"+filename), mode="r") as fails:
        count = int(fails.readline())
        main = list(map(int, fails.readline().split()))
        print(compute_height(count, main))
        

def compute_height(n, parents):
    zeros = np.zeros(n)
    def height(i):
        if zeros[i] != 0:
            return zeros[i]
        elif parents[i] == -1: 
            zeros[i] = 1
        else: 
            zeros[i] = height(parents[i]) + 1
        return zeros[i]

    for i in range(n):
        height(i)
    return max(zeros)

#     # input number of elements
#     # input values in one variable, separate with space, split these values in an array
#     # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
