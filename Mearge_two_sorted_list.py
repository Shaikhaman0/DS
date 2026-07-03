# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 21:06:37 2026

@author: aman
"""

# merge two sorted list
l1=[1,3,5,7]
l2=[2,4,6,8]

merge=[]
i=0
j=0

while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        merge.append(l1[i])
        i+=1
    else:
        merge.append(l2[j])
        j+=1
while i<len(l1):
    merge.append(l1[i])
    i+=1

while j<len(l2):
    merge.append(l2[j])
    j+=1        
print("merge list  is",merge)
