import numpy as np

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

print('----------- Método da potência inversa')

Ar1 = np.array([[5, 2, 1], [2, 3, 1], [1, 1, 2]], dtype='float64')
vr1 = np.random.rand(Ar1.shape[0])

print('Matriz A1')
result1r = reverse_power(Ar1, vr1, 0.000001)
print(f'Autovalor: {result1r[0]}')
print(f'Autovetor: {result1r[1]}')
print()

Ar2 = np.array([[-14, 1, -2], [1, -1, 1], [-2, 1, -11]], dtype='float64')
vr2 = np.random.rand(Ar2.shape[0])

print('Matriz A2')
result2r = reverse_power(Ar2, vr2, 0.000001)
print(f'Autovalor: {result2r[0]}')
print(f'Autovetor: {result2r[1]}')
print()

Ar3 = np.array([
  [40, 8, 4, 2, 1],
  [8, 30, 12, 6, 2],
  [4, 12, 20, 1, 2],
  [2, 6, 1, 25, 4],
  [1, 2, 2, 4, 5]], dtype='float64')
vr3 = np.random.rand(Ar3.shape[0])

print('Matriz A3')
result3r = reverse_power(Ar3, vr3, 0.000001)
print(f'Autovalor: {result3r[0]}')
print(f'Autovetor: {result3r[1]}')
print()

print('----------- Método da potência com deslocamento')

print('Matriz A1 e u = 7')
result1s = shifting_power(Ar1, vr1, 7.0, 0.000001)
print(f'Autovalor: {result1s[0]}')
print(f'Autovetor: {result1s[1]}')
print()

print('Matriz A2 e u = 11')
result2s = shifting_power(Ar2, vr2, -11.0, 0.000001)
print(f'Autovalor: {result2s[0]}')
print(f'Autovetor: {result2s[1]}')
print()

print('Matriz A3 e u = 22')
result3r = shifting_power(Ar3, vr3, 22.0, 0.000001)
print(f'Autovalor: {result3r[0]}')
print(f'Autovetor: {result3r[1]}')
print()
