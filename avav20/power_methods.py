import numpy as np

def regular_power(A, v0, eps = 0.000001):
  lmbda_old = 0
  lmbda_new = 0
  vk_old = np.zeros(A.shape[0])
  vk_new = np.copy(v0)

  x_old = np.zeros(A.shape[0])

  while True:
    lmbda_old = lmbda_new
    vk_old = np.copy(vk_new)

    x_old = vk_old / np.linalg.norm(vk_old)
    vk_new = np.dot(A, x_old)
    lmbda_new = np.dot(x_old.T, vk_new)

    err = abs((lmbda_new - lmbda_old) / lmbda_new)

    if (err <= eps): break

  return lmbda_new, x_old

def lu_decomp(A):
  n = A.shape[0]
  L = np.eye(n)
  U = np.copy(A)

  for k in range(n - 1):
    pivot = U[k, k]
    if pivot == 0:
      raise ValueError('Matriz não possui decomposição LU')
    
    for i in range (k+1, n):
      factor = U[i, k] / pivot
      L[i, k] = factor

      U[i, k:] -= factor * U[k, k:]

  return L, U

def lu_solve(L, U, b):
  n = L.shape[0]
  y = np.zeros(n)
  x = np.zeros(n)

  for i in range(n):
    y[i] = b[i] - np.dot(L[i, :i], y[:i])

  for i in range(n-1, -1, -1):
    x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

  return x

A = np.array([[2, -1, 3], [-4, 5, -1], [2, -2, 1]], dtype='float64')

def reverse_power(A, v0, eps = 0.000001):
  L, U = lu_decomp(A)

  lmbda_new = 0
  lmbda_old = 0

  vk1_old = np.zeros(A.shape[0])
  vk1_new = np.copy(v0)

  x = np.zeros(A.shape[0])

  while True:
    lmbda_old = lmbda_new
    vk1_old = np.copy(vk1_new)

    x = vk1_old / np.linalg.norm(vk1_old)
    vk1_new = lu_solve(L, U, x)
    lmbda_new = np.dot(x.T, vk1_new)

    err = abs((lmbda_new - lmbda_old) / lmbda_new)

    if (err <= eps): break

  lmbda_new = 1 / lmbda_new

  return lmbda_new, x

def shifting_power(A, v0, u, eps = 0.000001):
  A1 = A - (u * np.eye(A.shape[0]))

  lmbda1, x1 = reverse_power(A1, v0, eps)
  lmbda = lmbda1 + u

  return lmbda, x1