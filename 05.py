ksiazka_adresowa = []
nr_tel = []
osoba = ""
while osoba != "END":
    print("Książka", ksiazka_adresowa)
    osoba = input("Podaj imie (END = Koniec): ")
    if osoba == "END":
        break # wyskakujemy z pętli
    ksiazka_adresowa.append(osoba)

print("Cała książka:", ksiazka_adresowa)
ksiazka_adresowa.sort()
print("Cała książka:", ksiazka_adresowa)
