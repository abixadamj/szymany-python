ksiazka_adresowa = []
nr_tel = []
osoba = ""
numer = ""
while osoba != "END":
    print("Książka", ksiazka_adresowa)
    osoba = input("Podaj imie (END = Koniec): ")
    if osoba == "END":
        break # wyskakujemy z pętli
    numer = input("Nr telefonu: ")
    ksiazka_adresowa.append(osoba)
    nr_tel.append(numer)

print("Cała książka:", ksiazka_adresowa)
print("Numery:", nr_tel)
ksiazka_adresowa.sort()
print("Cała książka:", ksiazka_adresowa)
print("Numery:", nr_tel)
