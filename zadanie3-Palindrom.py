for j in range (0,30):
    l= j
    lstr = str(l)
    obrot=lstr[::-1]
    def powtorz(lstr,obrot):
        if obrot== lstr:
            print("Badana Liczba: ",lstr,"Jest palindromem\n")
        else:
            print("Badana Liczba: ",lstr,"nie jest palindromem!")
            nowyobrot = int(lstr)+int(obrot)
            print("Nowy obrot to:",lstr,"+",obrot,"=",nowyobrot)
            obrot = str(nowyobrot)
            lstr=obrot[::-1]
            powtorz(lstr,obrot)
    powtorz(lstr,obrot)


