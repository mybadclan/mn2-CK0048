import math

import closed
import opened

def integral(f, xi, xf, eps = 0.000001):
  area_old = 0
  n = 1
  error = math.inf

  while (error > eps):
    n *= 2
    deltaX = (xf - xi) / n
    area = 0

    for s in range(n-1):
      a = xi + s * deltaX
      b = xi + (s+1) * deltaX
      area += f(a, b)

    error = abs((area - area_old) / area)
    area_old = area

  return area_old

# closed



# execution

def example(x):
  aux = (math.sin(2*x) + (4*math.pow(x, 2)) + (3*x))

  return math.pow(aux, 2)

# closed
f_closed_by_trapeze = closed.integral_by_trapeze(example)
f_closed_by_simpson_1_3 = closed.integral_by_simpson_1_3(example)
f_closed_by_simpson_3_8 = closed.integral_by_simpson_3_8(example)
f_closed_by_creto_2_15 = closed.integral_by_booles(example)

result1c = f_closed_by_trapeze(0, 1)
result2c = f_closed_by_simpson_1_3(0, 1)
result3c = f_closed_by_simpson_3_8 = f_closed_by_simpson_3_8(0, 1)
result4c = f_closed_by_creto_2_15(0, 1)

print('Fórmula do Trapezio[FECHADO]   : {}'.format(round(result1c, 2)))
print('Fórmula de Simpson 1/3[FECHADA]: {}'.format(round(result2c, 2)))
print('Fórmula de Simpson 3/8[FECHADA]: {}'.format(round(result3c, 2)))
print('Fórmula de Creto 2/15[FECHADA] : {}'.format(round(result4c, 2)))

# opened
f_opened_by_trapeze = opened.integral_by_trapeze(example)
f_opened_by_milne = opened.integral_by_milne(example)
f_opened_by_creto_1 = opened.integral_by_creto_1(example)
f_opened_by_creto_2 = opened.integral_by_creto_2(example)

result1o = f_opened_by_trapeze(0, 1)
result2o = f_opened_by_milne(0, 1)
result3o = f_opened_by_creto_1(0, 1)
result4o = f_opened_by_creto_2(0, 1)

print('\nFórmula do Trapezio[ABERTA]   : {}'.format(round(result1o, 2)))
print('Fórmula de Simpson 1/3[ABERTA]: {}'.format(round(result2o, 2)))
print('Fórmula de Simpson 3/8[ABERTA]: {}'.format(round(result3o, 2)))
print('Fórmula de Creto 2/15[ABERTA] : {}'.format(round(result4o, 2)))