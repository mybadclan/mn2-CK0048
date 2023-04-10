import math

def derivative2Err4(f, x, deltaX = 0.5):
  f0 = (-15/8) * f(x)
  f1 = f(x + deltaX)
  f2 = f(x - deltaX)
  f3 = (-1/16) * f(x + (2*deltaX))
  f4 = (-1/16) * f(x - (2*deltaX))

  return (f0 + f1 + f2 + f3 + f4) * (4 / (3 * math.pow(deltaX, 2)))


def example(x):
  z0 = math.pow(math.e, 3 *x) + 4 * math.pow(x, 2)

  return math.sqrt(z0)


def converge():
  deltaX = 0.5
  error = math.inf
  fOld = derivative2Err4(example, 2, deltaX)

  print('value  = {}'.format(fOld))
  print('deltax = {}'.format(deltaX))
  print('error  = {}'.format(error))
  print('-----------------------------------')

  while (error > 0.00001):
    deltaX *= 0.5
    f = derivative2Err4(example, 2, deltaX)
    error = abs((f - fOld) / f)

    print('value  = {}'.format(f))
    print('deltax = {}'.format(deltaX))
    print('error  = {}'.format(error))
    print('-----------------------------------')

    fOld = f


converge()
