koniec_przedzialu = int(input("Podaj koniec przedzialu: "))
lista = []
lista_new = []

def stworzliste(koniec_przedzialu):
    for i in range (2,koniec_przedzialu+1):
        minimum = min(i,koniec_przedzialu)
        lista.append(minimum)

stworzliste(koniec_przedzialu)
print ("Podany przedzial zawiera liczby:")
print (lista)
print("Z tego przedzialu liczby pierwsze to:")


def program(argument,lista):

    print(argument)
    lista_new = []

    for j in range (0, len(lista)):

        if int(lista[j]) % argument != 0:

            lista_new.append(int(lista[j]))


    for k in range (0,len(lista_new)):
        lista[k] = lista_new[k]

    argument = int(lista[0])
    wielkosclisty = int(len(lista_new))

    if wielkosclisty > 0:
        program(argument,lista[0:len(lista_new)])
    else:
        print('koniec')

program(2,lista)
