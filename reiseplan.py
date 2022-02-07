
reisemål = [] 
for i in range(5): 
 reisemål.append(input("Skriv inn dine reisemål: ")) 
 
print(reisemål)
 
outfit = [] 
for i in range(5): 
 outfit.append(input("Skriv inn dine klesplagg: ")) 
 
print(outfit)
 
avreise = [] 
for i in range(5): 
 avreise.append(input("Når reiser du?: ")) 


 
reiseplan = reisemål, outfit, avreise
for i in reiseplan:
 print(i)

førsteliste= int(input("skrivv inn din første indeks: "))
if førsteliste<=2:
  print(reiseplan[førsteliste])
  valg=(reiseplan[førsteliste])
andreliste= int(input("skrivv inn din andre indeks: "))
if andreliste<=4:
  print(valg[andreliste])
if type(førsteliste) == int:
    print(reiseplan[1])
else:
  print("Ugyldig Input!")
if type (andreliste) == int:
  print(reiseplan[2])
else:
  print("Ugyldig Input!")
