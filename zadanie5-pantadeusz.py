plik=open("pan-tadeusz.txt","r",encoding="UTF-8")
# otwieramy plik, litera r oznacza czytanie (read) pliku, kodowanie znakow

slownik={}
#tworzymy slownik do ktorego bedzie wrzucany wyraz oraz jego ilosc

for wiersz in plik:
    #tekst oznacza tekst z otwartego pliku zapisanego w plik

    wiersz=wiersz[:-1]
    # kazdy wiersz pozbawiamy ostatniego znaku zeby uniknac enterow

    wiersz=wiersz.strip("\n").lower()
    #z konca wiersza usuwam znak nowej lini, z calego surowego tekstu ucinamy ciag znakow /n

    wyrazy= wiersz.split()
    #wyraz dzielimy na pojedyncze slowa

    for wyraz in wyrazy:
         dlugosc_wyrazu= len(wyraz)
         slownik.setdefault(wyraz,0)
         slownik[wyraz]=slownik[wyraz]+1
    #endfor

#endfor

lista=slownik.items()
#lista wszystkich itemow slownika "slownik" w parach wyraz:ilosc

lista_posortowana=sorted(lista,key=lambda k:k[1],reverse=True)
print("Lista wyrazów:\n")
for k,wiersz in lista_posortowana:
    print(k,wiersz)

plik.close() #zamykamy plik
