wynik = 0
i=0
while True:



    ilosc_znakow = str(i)
    dlugosc_konkretnej_liczby = len(str(i))


    rezultat = 0
    #print("licze!")
    for j in range (0,dlugosc_konkretnej_liczby):

        wynik = 0
        wynik = int(ilosc_znakow[j])**int(dlugosc_konkretnej_liczby)
        #print("Wynik:",wynik)

        rezultat = rezultat + wynik

    if rezultat == i:

        print ("Liczba armstronga wynosi:",i,"jej rezultat to:",rezultat)

    i = i +1