# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:33:23 2020

@author: Akshat Jain
"""



class Count(object):
    def count_subset(self , arr , sum , n ,t):
        for i in range(n+1):
            for j in range(sum+1):
                if i == 0 :
                    t[i][j] = 0
                if j == 0 :
                    t[i][j] = 1
                    
        
        for i in range(1 , n+1):
            for j in range(1,sum+1):
                if arr[i-1]<=j:
                    t[i][j] = (t[i-1][j-arr[i-1]] + t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][sum]
   
#count the number of subset with a given diffrence
import numpy as np
if __name__ == "__main__":
    arr = [1,1,2,3]
    n = len(arr)
    diff = 1
    total = 0
    for i in arr:
        total += i
    sum = int((total+diff)/2)
    t = np.zeros([n+1 , sum+1] , dtype = int)
    c = Count()
    print(c.count_subset(arr , sum , n ,t))    