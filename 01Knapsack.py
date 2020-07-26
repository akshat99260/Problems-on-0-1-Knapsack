# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:19:14 2020

@author: Akshat Jain
"""
import numpy as np
class Knapsack(object):
    t = np.ones([102 , 1001] , dtype = int)*-1
    def knapsack(self , wt , val , W , n):
        if n==0 or W==0:
            return 0 
        if Knapsack.t[n][W]!=-1:
            return Knapsack.t[n][W]
        if wt[n-1]<=W:
            Knapsack.t[n][W] = max(int(val[n-1] + self.knapsack(wt , val , W-wt[n-1] , n-1)) , int(self.knapsack(wt , val , W , n-1)))
            return Knapsack.t[n][W]
        else:
            Knapsack.t[n][W] = self.knapsack(wt , val , W , n-1)
            return Knapsack.t[n][W]
        
        
if __name__ == "__main__":
    val = [100 , 280 , 120] 
    wt = [10 , 40, 20] 
    W = 60
    n = len(val)
    knap = Knapsack()
    print("The Maximum profit will be " + str(knap.knapsack(wt , val , W , n)))
            
            