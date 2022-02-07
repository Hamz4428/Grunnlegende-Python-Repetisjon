def tall():
  Alder=int(input("skriv inn en alder "))
  Navn=str(input("Skriv inn et navn ")) 
  billetpris=()
  if Alder<17:
    billetpris=("30")
  elif Alder<63:
    billetpris=("50")
  elif Alder>=63:
    billetpris=("35")
  print("Hei",Navn,"Din bilett koster",billetpris)
tall()


