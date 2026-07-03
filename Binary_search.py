# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 20:58:06 2026

@author: aman
"""

# h2) Binary Search First Price >= 50000
price=[20000,30000,40000,50000,60000]
t=50000

l=0
h=len(price)-1


while l<=h:
    mid=(l+h)//2
    
    if price[mid]<t:
        l=mid+1
    else:
        h=mid-1
print("first price ",price[l])
