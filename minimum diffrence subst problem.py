# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:23:00 2020

@author: Akshat Jain
"""

class Minimum_sum(object):
    def subset_sum(self ,arr , sum ,n, t):
        for i in range(n+1):
            for j in range(sum+1):
                if i==0:
                    t[i][j] = False
                if j==0:
                    t[i][j] = True
            
        for i in range(1 , n+1):
            for j in range(1 , sum+1):
                if arr[i-1]<=j:
                    t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        half = int(sum/2)
        lst = []
        for j in range(sum+1):
            if t[n][j] == True and j <= half:
                lst.append(j)
                
        mn = sys.maxsize
        for i in lst:
            mn = min(mn , sum - 2*i)
        return mn
            
import sys
import numpy as np
import time
start_time = time.time()
if __name__ == "__main__":
    arr = [1,6,11,5]
    n = len(arr)
    sum = 0
    for i in arr:
        sum = sum+i
    t = np.zeros([n+1 , sum+1] , dtype = bool)
    mn = Minimum_sum()
    print(mn.subset_sum(arr , sum , n , t))
    mn.subset_sum
print("--- %s seconds ---" % (time.time() - start_time))