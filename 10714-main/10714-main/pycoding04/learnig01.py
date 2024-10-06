a = ['김치', '황기']
print(list(a))

for a in range(0,3,1):
  print(a)
  
  
  
for i,v in enumerate(a):
  if v == '배':
    a[i] = 0
    break
print(a)  

print()