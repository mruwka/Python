from turtle import *
import math

a = int(input("wprowadz poczatek przedzialu: "))
b = int(input("wprowadz koniec przedzialu: "))

wzor = input("podaj wzor funkcji: f(x)= ")
print ("Podany wzor: f(x)= ",wzor)

print("podany przedzial wynosi od",a,"do",b)

#rysujemy wykres
color('black')
forward(400)
write("x")
backward(800)
forward(400)
left(90)
forward(400)
write("y")
backward(800)
forward(400)
right(90)
backward(400)

#rysujemy funkcje
color('red')
up()
goto(a,0)
for x in range (a,b):
    y =eval(wzor)
    goto(x,y )
    down()
down()
done()