import math

def xk(xi, xf):
  def aux(alpha):
    return ((xi+xf)/2) + ((xf-xi)/2)*alpha
  
  return aux

WEIGHTS = {
  2: [1, 1],
  3: [5/9, 8/9, 5/9],
  4: [0.34785, 0.65215, 0.65215, 0.34785]
}

ROOTS = {
  2: [-math.sqrt(1/3), math.sqrt(1/3)],
  3: [-math.sqrt(3/5), 0, math.sqrt(3/5)],
  4: [
    -math.sqrt((3+2*math.sqrt(6/5))/7),
    -math.sqrt((3-2*math.sqrt(6/5))/7),
     math.sqrt((3-2*math.sqrt(6/5))/7),
     math.sqrt((3+2*math.sqrt(6/5))/7)
  ]
}

def integralCalc(fn, xi, xf, g):
  k_aux = (xf - xi) / 2
  roots = ROOTS[g]
  weight = WEIGHTS[g]

  fn_xk = xk(xi, xf)

  result = 0
  for i in range(g):
    x = fn_xk(roots[i])
    wk = weight[i]
    result += (fn(x)*wk)
  
  return k_aux * result

# Exemplo

def example(x):
  aux = math.sin(2*x) + (4*math.pow(x,2)) + (3*x)
  return math.pow(aux, 2)

result_G2 = integralCalc(example, 0, 1, 2)
result_G3 = integralCalc(example, 0, 1, 3)
result_G4 = integralCalc(example, 0, 1, 4)

print('Resultado com Gauss-Legendre 2: {}'.format(result_G2))
print('Resultado com Gauss-Legendre 3: {}'.format(result_G3))
print('Resultado com Gauss-Legendre 4: {}'.format(result_G4))

def integral(f, xi, xf, g, eps = 0.000001):
  area_old = 0
  n = 1
  error = math.inf
  it = 0

  while (error > eps):
    n *= 2
    deltaX = (xf - xi) / n
    area = 0

    for s in range(n):
      a = xi + s * deltaX
      b = a + deltaX
      area += integralCalc(f, a, b, g)

    error = abs((area - area_old) / area)
    area_old = area
    it += 1

  return [area_old, n, it]

print('Estratégia por partição')


result_part_G2 = integral(example, 0, 1, 2)
result_part_G3 = integral(example, 0, 1, 3)
result_part_G4 = integral(example, 0, 1, 4)

print('Resultado com Gauss-Legendre 2: {}'.format(result_part_G2))
print('Resultado com Gauss-Legendre 3: {}'.format(result_part_G3))
print('Resultado com Gauss-Legendre 4: {}'.format(result_part_G4))