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

  return [lmbda_new, x_old]

m1 = np.array([[5, 2, 1], [2, 3, 1], [1, 1, 2]])
v1 = np.random.rand(m1.shape[0])
result1 = regular_power(m1, v1)

print('Exemplo 1')
print(f'Autovalor dominante {result1[0]}')
print(f'Autovetor {result1[1]}')

m2 = np.array([[40, 8, 4, 2, 1],
               [8, 30, 12, 6, 2],
               [4, 12, 20, 1, 2],
               [2, 6, 1, 25, 4],
               [1, 2, 2, 4, 5]])
v2 = np.random.rand(m2.shape[0])
result2 = regular_power(m2, v2)

print('Exemplo 2')
print(f'Autovalor dominante {result2[0]}')
print(f'Autovetor {result2[1]}')

