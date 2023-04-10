def integral_by_trapeze(f):
  def f_aux(a, b):
    aux = (b - a) / 2
    return (f(a) + f(b)) * aux

  return f_aux

def integral_by_simpson_1_3(f):
  def f_aux(a, b):
    h = (b - a) / 2
    values = [1, 4, 1]
    area = 0

    for s in range(len(values)):
      x = a + (s * h)
      area += (values[s] * f(x))

    return (h/3) * area

  return f_aux

def integral_by_simpson_3_8(f):
  def f_aux(a, b):
    h = (b - a) / 3
    values = [1, 3, 3, 1]
    area = 0

    for s in range(len(values)):
      x = a + (s*h)
      area += (values[s] * f(x))

    return ((3*h)/8) * area

  return f_aux

def integral_by_booles(f):
  def f_aux(a, b):
    h = (b-a)/4
    values = [7, 32, 12, 32, 7]
    area = 0

    for s in range(len(values)):
      x = a + (s*h)
      area += (values[s] * f(x))

    return ((2*h)/45) * area

  return f_aux

