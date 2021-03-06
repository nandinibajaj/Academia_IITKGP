# -*- coding: utf-8 -*-
"""ComputationalChemistry_Lab6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1idkTIkbhWS9wRm5Gxb6m4SA8khnOD9hA

**Nandini Bajaj 18CY20020**

Lab Assignment 6
"""

import pandas as pd
import numpy as np
import math
import random
import matplotlib.pyplot as plt

#12 - 6 lennard jones
def lennard_jones(r, m = 12, n = 6):
    if r>=rc:     
        return 0
    a1 = sig/r
    a = 4*eps*(pow(a1,m)-pow(a1,n))
    return a

def force_cal(dis):
  if (dis >= sig and dis <= rc ):
    v1 = 12 * (pow(sig, 12) / pow(dis, 13))
    v2 = 6 * (pow(sig, 6) / pow(dis, 7))
    return 4 * eps * (v1 - v2)
  return 0

def pbc(n,r):
  if data1.iloc[n][r] > l / 2:
    data1.iloc[n][r] -= l
  elif data1.iloc[n][r] < -l / 2:
    data1.iloc[n][r] += l

def minimum_image_convention(dis, L):
    if dis > L/2:
        dis = dis - L
    elif dis <= -L/2:
        dis = dis + L
    return dis

def distance_in_3D(i,j):
    x1 = data1.iloc[i][0]
    y1 = data1.iloc[i][1]
    z1 = data1.iloc[i][2]
    x2 = data1.iloc[j][0]
    y2 = data1.iloc[j][1]
    z2 = data1.iloc[j][2]

    dx=minimum_image_convention(x1-x2, L)
    dy=minimum_image_convention(y1-y2, L)
    dz=minimum_image_convention(z1-z2, L)

    r=math.sqrt(dx**2 + dy**2 + dz**2)
    return lennard_jones(r)

def verlet(iter, j, fx, fy, fz):
  if iter==0:
    data1.iloc[j][0] += 0.5* (fx/ m) * dt * dt
    data1.iloc[j][1] += 0.5* (fy/ m) * dt * dt
    data1.iloc[j][2] += 0.5* (fz/ m) * dt * dt

  else:
    tx = 2*data1.iloc[j][0] - data.iloc[j][0] + 0.5*(fx/ m) * dt * dt
    ty = 2*data1.iloc[j][1] - data.iloc[j][1] + 0.5*(fy/ m) * dt * dt
    tz = 2*data1.iloc[j][2] - data.iloc[j][2] + 0.5*(fz/ m) * dt * dt

    data.iloc[j][0]=data1.iloc[j][0]
    data.iloc[j][1]=data1.iloc[j][1]
    data.iloc[j][2]=data1.iloc[j][2]   

    data1.iloc[j][0]=tx
    data1.iloc[j][1]=ty
    data1.iloc[j][2]=tz

data = pd.read_csv("/content/argon_data.csv")
data1 = data.copy()

sig=float(input("Enter the value of sigma:"))
eps=float(input("Enter the value of epsilon:"))
L=float(input("Enter the cell dimension:"))
rc=float(input("Enter the cut-off radius:"))
dt=float(input("Enter the time step(dt):"))

pr_ma=1.673*pow(10,-27)
m=40*pr_ma
l=L

N = 365
for i in range(10):
  for j in range(N):
    pbc(j,0)
    pbc(j,1)
    pbc(j,2)

  for p in range(N-1):
    f=0.0
    fx=0.0
    fy=0.0
    fz=0.0
    dis=0.0
    for q in range(p+1, N):
      dis = distance_in_3D(p,q)
      f = force_cal(dis)

      if dis !=0:
        fx=fx+ abs(f/dis)*data.iloc[p][0]
      else:
        fx=fx+0

      if dis !=0:
        fy=fy+ abs(f/dis)*data.iloc[p][1]
      else:
        fy=fy+0

      if dis !=0:
        fz=fz+ abs(f/dis)*data.iloc[p][2]
      else:
        fz=fz+0

  for j in range(N):  
    #verlet(i,j, fx, fy, fz) 
       

print('The coordinates of the particle after 10 iterations:')
for i in range(N):
  print(data1.iloc[i][0], data1.iloc[i][1], data1.iloc[i][2])        
return 0

data1.to_csv("final_coordinates.csv", index=False)

data1

