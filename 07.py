ksiazka_adresowa = []
while True:
    print("Książka", ksiazka_adresowa)
    osoba = input("Podaj imie (END = Koniec): ")
    if osoba == "END":
        break # wyskakujemy z pętli
    ksiazka_adresowa.append(osoba)

print("Cała książka:", ksiazka_adresowa)
ksiazka_adresowa.sort()
print("Cała książka:", ksiazka_adresowa)

for element in ksiazka_adresowa:
    print("Osoba:", element)
    if element[-1:] == "a":
        print("To chyba dziewczyna")





