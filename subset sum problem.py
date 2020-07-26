 # -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:07:08 2020

@author: Akshat Jain
"""
import numpy as np
''' SubSet Sum Problem '''

class Subset(object):
    def subset(self , arr , sum ,n, t):
        for i in range(n+1):
            for j in range(sum+1):
                if i == 0:
                    t[i][j] = False
                if j == 0:
                    t[i][j] = True
        for i in range(1,n+1):
            for j in range(1 ,sum+1):
                if arr[i-1]<=j:
                    t[i][j] = (t[i-1][j-arr[i-1]] or t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][sum]


if __name__ == "__main__":
    arr = [10 , 30,30,40,50]
    sum = 5
    n = len(arr)
    t = np.zeros([n+1 , sum+1] , dtype = bool)
    sub = Subset()
    print(sub.subset(arr , sum , n,t))