mineOrd=[]
def  slaaSammen():
  st1=("streng 1,")
  st2=("streng 2")
  print(st1+st2)
slaaSammen()
mineord2=[1,2,3,4,5,]
def skrivUT():
  for x in range(len(mineord2)):
    print (mineord2[x],)
skrivUT()

while True:
    n = (input('skriv inn en streng: '))

    if n =="i":
      a=(input('skriv inn din første streng: '))
      b=(input('skriv inn din andre streng: '))
    def slaaSammen(a,b):
      sammen=(a+b)
      mineOrd.extend((sammen))

    slaaSammen(a,b)

    if n=="u":
      def skrivUT(mineOrd):

        print(mineOrd)
      skrivUT(a+b)
    elif n =="s":
      break


