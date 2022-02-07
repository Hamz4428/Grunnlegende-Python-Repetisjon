def innlesning(filnavn):
  data = {}
  filnavn = open("salgstall.txt", "r")
  for line in filnavn:
      (val, key) = line.split()
      data[str(val)] = key
  for key, value in data.items():
    print(key, ' : ', value)
  return data
innlesning("")
def maanedensSalg(data):
  maximum= max(data, key=data.get)
  print(maximum, data[maximum])
maanedensSalg({"Heidi":133,"John":97,"kari":48})
def totaltAntallSalg(data):
  tall=sum(data.values())
  print(tall)
totaltAntallSalg({"Heidi":133,"John":97,"kari":48})
def gjennomsnittSalg(data):
  filtered_vals = [v for _, v in data.items() if v != 0]
  average = sum(filtered_vals) / len(filtered_vals)
  print(average)
gjennomsnittSalg({"Heidi":133,"John":97,"kari":48})
def hovedprogram():
  print("Maanedens ansatte"),maanedensSalg({"Heidi":133,"John":97,"kari":48})
  print("Aktive selgere denne mååneden er  3 med"),totaltAntallSalg({"Heidi":133,"John":97,"kari":48})
  print("Gjennomsnittlig antall salg per salgsperson:"),gjennomsnittSalg({"Heidi":133,"John":97,"kari":48})
hovedprogram()
