# -*- coding: utf-8 -*-
"""Lab3_ComputationalChemistry.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1URnRaICw45GgDINsMwg_YC221u99deCd
"""



"""**NANDINI BAJAJ 18CY20020**

Laboratory Assignment 3
"""

import pandas as pd
import numpy as np
import math
import random
import matplotlib.pyplot as plt

data = pd.read_csv("/content/sample_data/input_data.csv") #saved the model.txt file provided into csv and then import

def pbc_on_one_particle(x, y, z):
        L = 18.64
        applied_pbc = False
        if x>L/2: 
            x = x - L
            applied_pbc = True
        elif x<= -L/2:
            x = x + L
            applied_pbc = True
        
        if y > L/2: 
            y = y - L
            applied_pbc = True
        elif y<= -L/2: 
            y = y + L
            applied_pbc = True
            
        if z > L/2: 
            z = z - L
            applied_pbc = True
        elif z<= -L/2: 
            z = z + L
            applied_pbc = True
        
        return x,y,z, applied_pbc

def pbc(df, n):
    ans = 0      #total number of pbc appplied in 1 iteration
    for i in range(n):
        #choosing in which direction particle should be moved
        coordinate_choosing = random.randint(1, 3)    # to generate either 1,2 or 3
                                                  # 1 for change in x, 2 for y and 3 for z
        directional_choosing = random.randint(1,2)    # to generate either 1 or 2
                                                  # 1 for +1 ams and 2 for -1ams
    
        x = df.iloc[i][0]
        y = df.iloc[i][1]
        z = df.iloc[i][2]
        
        if(coordinate_choosing == 1):
            if(directional_choosing == 1):
                x = x + 1
            else:
                x = x - 1
                
        elif(coordinate_choosing == 2):
            if(directional_choosing == 1):
                y = y + 1
            else:
                y = y - 1
                
        elif(coordinate_choosing == 3):
            if(directional_choosing == 1):
                z = z + 1
            else:
                z = z - 1
        
        x, y, z, applied_pbc = pbc_on_one_particle(x ,y, z)
        df.iloc[i][0] = x
        df.iloc[i][1] = y
        df.iloc[i][2] = z
        if(applied_pbc == True):
            ans += 1
    
    return df, ans

def start_the_routine(df):
    for i in range(20):
        df, pbc_count_in_one_iteration = pbc(df, data.shape[0])
        print("Number of molecules that experienced PBC in iteration ", i+1," = ", pbc_count_in_one_iteration)
        if(i == 4):
            df.to_csv("iteration_5.csv")
        elif(i == 9):
            df.to_csv("iteration_10.csv")
        elif(i == 19):
            df.to_csv("iteration_20.csv")

data_copy = data.copy()
start_the_routine(data_copy)





















