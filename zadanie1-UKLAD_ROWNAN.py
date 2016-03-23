import math as m
print ("Dany jest uklad rownan:")
print ("Ax+By=C")
print ("Dx+Ey=F")
print("")
#wyswietlamy informacje o układzie równan

a = float(input("podaj A ")) # wprowadzi liczbe a
b = float(input("podaj B ")) # wprowadzi liczbe b
c = float(input("podaj C ")) # wprowadzi liczbe c
d = float(input("podaj D ")) # wprowadzi liczbe d
e = float(input("podaj E ")) # wprowadzi liczbe e
f = float(input("podaj F ")) # wprowadzi liczbe f
#wprowadzamy wartosici poszczegolnych liczb

print ("Uklad rownan wynosi:\n",a,"x +",b,"y =",c,"\n",d,"x +",e,"y =",f)
#wyswietlamy układ rownan

wyznacznik = a * e - b * d
print("")
print ("Wyznacznik jest równy:", wyznacznik)
#wyswietlamy wyznacznik

wyznacznikx = c * e - b * f
wyznaczniky = a * f - c * d
print ("Wyznacznik X to:", wyznacznikx)
print ("Wyznacznik Y to:", wyznaczniky)
#wyswietlamy wyznaczniki


if wyznacznik != 0:
  print ("Uklad jest oznaczony")
  rozwiazaniex = wyznacznikx/wyznacznik
  rozwiazaniey = wyznaczniky /wyznacznik
  print ("Rozwiazanie: x jest równe:",rozwiazaniex," a Y jest równy:",rozwiazaniey)
#liczymy równaine jezeli wynik jest różny od zera

elif wyznacznik == 0 and (wyznacznikx!= 0 or wyznaczniky !=0):
  print ("Ukald jest sprzeczny!")
#wyswietalmy gdy układ jest sprzeczny

else:
  print ("Uklad jest nieoznaczony!")
#układ nieoznaczony

