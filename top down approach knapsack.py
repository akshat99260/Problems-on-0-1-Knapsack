# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:07:09 2020

@author: Akshat Jain
"""
import numpy as np
class Knapsack(object):
    def knapsack(self , wt , val , W , n , t):
        for i in range(n+1):
            for j in range(W+1):
                if i==0 or j==0:
                    t[i][j] = 0
                j = j+1
            i = i+1
        for i in range(1 ,n+1):
            for j in range(1 ,W+1):
                if wt[i-1]<=j:
                    t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]] , t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        
        return t[n][W]
                    
        
        
        
        
        
if __name__ == "__main__":
    val = [100 , 280 , 120] 
    wt = [10 , 40, 20] 
    W = 60
    n = len(val)
    t = np.ones([n+1 , W+1] , dtype = int)
    knap = Knapsack()
    print("The Maximum profit will be " + str(knap.knapsack(wt , val , W , n , t)))
            