

def cigar_party(cigars, is_weekend):
  if is_weekend and 40 <= cigars:
    return True
  elif 60 >= cigars >= 40:
    return True
  return False
