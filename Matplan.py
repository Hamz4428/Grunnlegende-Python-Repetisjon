
thisdict = {
  "Hamza": "brød til frokost"", egg til lunsj"", pølser til middag",
  "Adam":"cornflakes til frokost"", scampi til lunsj"", couscous til middag",
  "Kari":"knekkebrød til frokost"", salat til lunsj"", taco til middag",
  }
allepar = list(thisdict.items())
def matplan():
  for key, value in thisdict.items() :
    print (key)
  frabruker=input("skriv inn navet til en beboer ")
  if frabruker in thisdict:
    print(thisdict[frabruker])
  else:
    print(f"Nei: '{frabruker}' finnes ikke i ordboken")
matplan()