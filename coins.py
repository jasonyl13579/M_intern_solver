# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 00:39:29 2020

@author: Corn
"""

cases = input()

for case in range(int(cases)):
    text = input()
    n, m = text.split()
    m = int(m)
    coins = [int(i) for i in input().split()]
    dp = [float('inf')]* (m+1)
    dp[0] = 0
    for i in range(1, m+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1) 
    print (dp[m] if dp[m] != float('inf') else -1)