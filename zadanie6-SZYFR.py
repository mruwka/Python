import string
alfabet = list(dict.fromkeys(string.ascii_lowercase, 0))
alfabet.sort()
# importujemy alfabet


slowo = str(input("Podaj slowo: "))
# wprowadzi slowo do zaszyfrowania



liczba = str(input("Podaj liczbe: ")) # wprowadzi slowo do zaszyfrowania
# liczba do szyfrowania

print ("OTO ZASZYFROWANE SLOWO",slowo,":",)

slowo = slowo.lower()
# slowo zmieniamy na male litery w celu eliminacji ewentualnych niezgodnosci z alfabeterm ktory zawiera same male litery


slowo_dlugosc =  len(slowo)
# dlugosc slowa (ilosc liter)

liczba_dlugosc = len(liczba)
# dlugosc liczby

powtorzenie = int(slowo_dlugosc) // int (liczba_dlugosc)
#calkowity wynik z dzielenia dlugosci slowa przez dlugosc liczbu


nowaliczba=""
#nowa liczba ktora bedzie konkatynacja powtorzen liczby szyfrowanej
# dzieki temu przypiszemy jej powtorzenie odpowiednio wiele razy


for i in range  (0,powtorzenie+1) :
    nowaliczba += liczba
    #tworzymy nowa liczbe powtarzajac stara liczbe

litery = list(slowo)
# lista liter w slowie

cyfry=list(nowaliczba)
# lsita cyfr w licbie




for i in range (0,slowo_dlugosc):
    # for wykona sie tak wiele razy ile jest liter w slowie

    for j in alfabet:
        #bierzemy caly alfabet

        if j == str(litery[i]):
            # jezeli j-ta litera w alfabecie jest taka sama jak litera i-ta w naszym slowie to:

            miejsce = int(cyfry[i]) + int(str(alfabet.index(j)))
            #zwiekszamy index naszej litery w alfabecie o wartosc cyfry przyporzadkowanej mu w szyfrze

            #print (litery[i],cyfry[i],str(alfabet.index(j)),str(alfabet[miejsce]))
            # testowy print, pozwalajacy sprawdzic, czy nasz program dziala, nie usuwac (NIGDY)

            print(str(alfabet[miejsce]))
            #drukujemy zaszyfrowane slowo
