# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 20:53:15 2026

@author: afzal
"""

# h1) Linear Search - Spam Detector

list=[101,102,300,500,600]
id=int(input("enter sender id "))
found=0
for i in list:
    if i == id:
        found=1
        break
if found==1:
    print("spam sender found")
else:
    print("not spam found")
