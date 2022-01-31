def sum(n):
  if n == 1:
    return
  
  return sum(n) + sum(n-1)

print(sum(4))