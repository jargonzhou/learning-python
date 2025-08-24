"""
Common procedures.
"""


def fixed(o):
  """whether has a fixed value"""
  try:
    hash(o)
  except TypeError:
    return False
  return True
