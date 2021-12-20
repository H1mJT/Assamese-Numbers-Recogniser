# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 16:45:44 2021

@author: Himjyoti
"""

def to_english(response):
    if response=="১": q=1
    elif response=="২": q=2
    elif response=="৩": q=3
    elif response=="৪": q=4
    elif response=="৫": q=5
    elif response=="৬": q=6
    elif response=="৭": q=7
    elif response=="৮": q=8
    elif response=="৯": q=9
    else: q=0
    return q
