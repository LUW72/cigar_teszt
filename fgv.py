

def cigar_party(cigars, is_weekend):
  if is_weekend and 40 <= cigars:
    return True
  elif 60 >= cigars >= 40:
    return True
  return False

def hazi_test(a, b):
  sum:int = a + b
  if 10 <= sum <= 19:
    return 20
  return sum