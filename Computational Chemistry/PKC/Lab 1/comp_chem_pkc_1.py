#Nandini Bajaj
#18CY20020
#Lab assignment 1

import math

def iterative(x):
  nerr = 1
  i = 0
  while(nerr >= 1e-6):
    c = math.exp(math.sin(x))
    xi = (-b - math.sqrt((b**2) - (4*a*c))) /(2*a)
    i = i+1
    print("Iteration:",i," value of x is: ",x)
    nerr = abs(x - xi)/x
    x = xi

  return x

def func(x):
  return a*x*x + b*x + math.exp(math.sin(x))
 
def derivative(x):
  return 2*a*x + b + math.cos(x)*math.exp(math.sin(x))
 
def newtonRaphson(x):
  i = 0
  h = func(x) / derivative(x)
  while abs(h/x) >= 1e-6:
    h = func(x)/derivative(x)
    x = x-h
    i = i+1
    print("Iteration:",i," value of x is: ",x)


# Initial values
x0 = 10 
a = 4
b = -6
x = iterative(x0) #iterative method
print("The final value of x by iterative method is: ",x)
print("\n")
newtonRaphson(x0) #newton raphson method
print("The final value of x by newton raphson is: ",x)
