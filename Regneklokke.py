lst = []
 
while True:
 try: 
   lst.append(int(input("skriv inn et tall: ")))
 except ValueError:
   print("jeg forstod ikke ")
 if lst[-1] == 0:
  break
 
minSum = sum(lst)
minsteTall = min(lst)
størsteTall = max(lst)
 
print("Summen av tallene: ", minSum)
print(minsteTall, "\n", størsteTall, sep="")


