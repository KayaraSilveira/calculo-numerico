# Imports
from sympy import *
import math
import numpy as np
import copy

# ------------------------------------------------------
# Gauss
def gauss(matriz):
  for i in range(len(matriz)):
    for j in range(len(matriz) + 1):
      if i == j:
        for k in range(i + 1, len(matriz)):
          if(matriz[i][j] == 0):
            print("Não é possível utilizar o método de Gauss pois há um pivô zero")
            return -1
          m = matriz[k][j]/matriz[i][j]
          for l in range(len(matriz) + 1):
            matriz[k][l] = matriz[k][l] - m * matriz[i][l]
  print("Matriz escalonada:")
  print(matriz)
  print("Resultados:")
  retro(matriz)

# ---------------------------------------------------------
# Retro substituição
def retro(matriz):
    x = np.zeros((1, len(matriz)))
    for i in range(len(matriz) - 1, -1, -1):
        for j in range(len(matriz) - 1, -1, -1):
            aux = 0
        if i == j:
            if(i == (len(matriz) - 1)):
                x[0][i] = matriz[i][j + 1]/matriz[i][j]
            else:
                for k in range((j + 1), len(matriz)):
                    aux = aux + matriz[i][k] * x[0][k]
                    x[0][i] = (matriz[i][len(matriz)] - aux)/matriz[i][j]
    for i in range(0, len(matriz)):
        print("{:.5f}".format(x[0][i]))