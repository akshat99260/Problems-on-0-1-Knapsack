# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:38:19 2020

@author: Akshat Jain
"""

import numpy as np
'''count of SubSet Sum Problem '''

class Subset(object):
    def subset(self , arr , sum ,n, t):
        for i in range(n+1):
            for j in range(sum+1):
                if i == 0:
                    t[i][j] = 0
                if j == 0:
                    t[i][j] = 1
        for i in range(1,n+1):
            for j in range(1 ,sum+1):
                if arr[i-1]<=j:
                    t[i][j] = (t[i-1][j-arr[i-1]] + t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][sum]


if __name__ == "__main__":
    arr = [1 , 2,3,4,5]
    sum = 7
    n = len(arr)
    t = np.zeros([n+1 , sum+1] , dtype = int)
    sub = Subset()
    print(sub.subset(arr , sum , n,t))