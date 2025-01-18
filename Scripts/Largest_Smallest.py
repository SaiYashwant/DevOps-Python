import os

def Small_Large(lists):
  min_elem = min(lists)
  max_elem = max(lists)
  return min_elem, max_elem

lists = [34,23,2,15,57]
min_elem, max_elem = Small_Large(lsits)
print(f"smallest elem: {min_elem} largest elem: {max_elem}")
