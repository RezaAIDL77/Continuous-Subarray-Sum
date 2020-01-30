#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, 
write a function to check if the array has a continuous subarray of 
size at least 2 that sums up to a multiple of k, that is, sums up to n*k 
where n is also an integer.

@author: rezarashetnia
"""

class Solution(object):
    def checkSubarraySum(self, A, k):
        p = [0]
        for x in A:
            v = p[-1]+x
            if k: v %= abs(k)
            p.append(v)
        
        seen = set()
        for i in range (len(p)-3,-1,-1):
            seen.add(p[i+2])
            if p[i] in seen:
                return True
        return False