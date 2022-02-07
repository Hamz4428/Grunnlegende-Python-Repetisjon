tempratur=[-1,-6,4,10,20,22,22,20,15,9,3,0]
for line in tempratur:
  print(line)
def liste():
  count = 0
  for i in tempratur:
      count += i
  avg = count/len(tempratur)
  print(avg)
liste()

  

