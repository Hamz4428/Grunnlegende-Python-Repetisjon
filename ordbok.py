
class_list = dict() 
handleliste= {"melk" : 14.90 , "brød" : 24.9 , "youghurt" : 12.9, "pizza": 39.9, "range" : 40}
for x, y in handleliste.items():
  print("{}: {}".format(x, y))
frabruker=input('skriv inn navn på to varer med : mellom dem  ')
frabrukerpris=int(input('skriv inn pris på to varer med : mellom dem  '))
handleliste[frabruker]=frabrukerpris
    # Displaying the dictionary 
for x, y in handleliste.items():
  print("{}: {}".format(x, y))
  