# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 14:59:00 2018

@author: Grani
"""

#%%
def bubble(lst):
    for j in range(0, len(lst) - 1):
        for i in range(0, len(lst) - j - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp