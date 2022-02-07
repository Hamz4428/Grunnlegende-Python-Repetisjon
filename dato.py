#oppgave 3
dag1=int(input("skriv inn din dags dato "))
måned1=int(input("skriv inn din måned "))
if måned1==1:
  print(dag1,"januar")
elif måned1==2:
  print(dag1,"februar")
elif måned1==3:
  print(dag1,"mars")
elif måned1==4:
  print(dag1,"april")
elif måned1==5:
  print(dag1,"mai")
elif måned1==6:
  print(dag1,"juni")
elif måned1==7:
  print(dag1,"juli")
elif måned1==8:
  print(dag1,"august")
elif måned1==9:
  print(dag1,"september")
elif måned1==10:
  print(dag1,"oktober")
elif måned1==11:
  print(dag1,"november")
elif måned1==12:
  print(dag1,"desember")
else:
  print("du har ikke skrivet inn en valid måned ")
dag2=int(input("skriv inn din dags dato "))
måned2=int(input("skriv inn din måned "))
if måned2==1:
  print(dag2,"januar")
elif måned2==2:
  print(dag2,"februar")
elif måned2==3:
  print(dag2,"mars")
elif måned2==4:
  print(dag2,"april")
elif måned2==5:
  print(dag2,"mai")
elif måned2==6:
  print(dag2,"juni")
elif måned2==7:
  print(dag2,"juli")
elif måned2==8:
  print(dag2,"august")
elif måned2==9:
  print(dag2,"september")
elif måned2==10:
  print(dag2,"oktober")
elif måned2==11:
  print(dag2,"november")
elif måned2==12:
  print(dag2,"desember")
else:
  print("du har ikke skrivet inn en valid måned ")
dato1=dag1+måned1
dato2=dag2+måned2
if dato1 > dato2:
  print("feil rekkefølge")
elif dato2>dato1:
  print("riktig rekkefølge")
elif dato1==dato2:
  print("samme dato! ")


