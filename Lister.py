my_list = [1, 2, 3]
print(my_list[0], my_list[2])
addisjon = 0
list = [1, 2, 3]
for x in list:
    addisjon += x
print(addisjon)
product = 1  
list = [2, 2, 3]
for x in list:
    product *= x
print(product)
ny_list1=[6,12]
ny_liste2=my_list + ny_list1
print(ny_liste2)
skalbort=[3]
for index in skalbort:
    del ny_liste2[index]
print(ny_liste2)
ny_liste2.pop()
print(ny_liste2)
ny_liste3=[]
frabruker=str(input("skrivv inn 4 navn: "))
ny_liste3.append(frabruker)
print(ny_liste3)
if frabruker=="hamza":
  print("du husket meg")
else:
  print("“Glemte du meg?”.")
