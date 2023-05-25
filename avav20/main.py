import numpy as np
import power_methods as pm

def householder_column(A, i):
  size = A.shape[0]

  I = np.eye(size)
  w = np.zeros(size)
  wi = np.zeros(size)

  w[i+1:] = A[i+1:, i]

  lw = np.linalg.norm(w)
  wi[i+1] = lw

  N = w - wi
  n = N / np.linalg.norm(N)

  h_aux = 2 * np.outer(n, n.T)
  H = I - h_aux

  return H

def householder(A):
  n = A.shape[0]

  H_old = np.eye(n)
  A_old = np.copy(A)

  A_new = np.copy(A)

  for i in range(n-2):
    H_new = householder_column(A_old, i)

    # print(f'Passo {i}')
    # print(H_new, H_new.shape)
    # print(A_old, A_old.shape)
    # print(np.round(np.matmul(np.matmul(H_new, A_old), H_new)), end='\n\n')

    A_new = np.matmul(np.matmul(H_new, A_old), H_new)
    A_old = A_new

    H_old = np.matmul(H_old, H_new)

  return A_old, H_old

A = np.array([
  [40, 8, 4, 2, 1],
  [8, 30, 12, 6, 2],
  [4, 12, 20, 1, 2],
  [2, 6, 1, 25, 4],
  [1, 2, 2, 4, 5]], dtype='float64')

A_barra, H = householder(A)
v1 = np.random.rand(A_barra.shape[0])

regular_lmbda, regular_v = pm.regular_power(A_barra, v1)
reverse_lmbda, reverse_v = pm.reverse_power(A_barra, v1)

def get_all_eigen(A_barra, H):
  lmbdas = []
  vs = []

  for i in range(0, int(regular_lmbda)):
    try:
      shifting_lmbda, shifting_v = pm.shifting_power(A_barra, v1, i)

      if (i == 0): 
        lmbdas.append(shifting_lmbda)
        vs.append(shifting_v)

      if (np.trunc(shifting_lmbda) == np.trunc(regular_lmbda)):
        lmbdas.append(shifting_lmbda)
        vs.append(shifting_v)
        break

      if (np.trunc(shifting_lmbda) != np.trunc(lmbdas[-1])):
        lmbdas.append(shifting_lmbda)
        vs.append(shifting_v)
    except:
      pass

  new_vs = []
  for v in vs:
    result = np.matmul(H, v)
    new_vs.append(result)

  return lmbdas, new_vs

lmbdas, vs = get_all_eigen(A_barra, H)

print(lmbdas)
for v in vs: print(v)



