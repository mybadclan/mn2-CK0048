def integral_by_trapeze(f):
  def f_aux(a, b):
    h = (b-a)/3
    values = [1, 1]
    area = 0

    for s in range(len(values)):
      x = (a + h) + (s*h)
      area += (values[s]*f(x))

    return ((3*h)/2) * area

  return f_aux

def integral_by_milne(f):
  def f_aux(a, b):
    h = (b-a)/4
    values = [2, -1, 2]
    area = 0

    for s in range(len(values)):
      x = (a+h) + (s*h)
      area += (values[s]*f(x))

    return ((4*h)/3)*area

  return f_aux

def integral_by_creto_1(f):
  def f_aux(a, b):
    h = (b -a)/5
    values = [11, 1, 1, 11]
    area = 0

    for s in range(len(values)):
      x = (a+h) + (s*h)
      area += (values[s]*f(x))

    return ((5*h)/24) * area

  return f_aux

def integral_by_creto_2(f):
  def f_aux(a, b):
    h = (b - a)/6
    values = [11, -14, 26, -14, 11]
    area = 0

    for s in range(len(values)):
      x = (a+h) + (s*h)
      area += (values[s]*f(x))

    return ((3*h)/10) * area

  return f_aux