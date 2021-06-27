# Tutaj pisz swój kod, młody padawanie ;-)
# akjsgfkasdjgfaksdh
print("Cześć!")
imie_osoby = input("Jak masz na imie? ")
print("Hello",imie_osoby,"ja to Python")
rok_urodzenia = int(input("Podaj rok urodzenia: "))
wiek = 2021 - rok_urodzenia
print("Masz",wiek,"lat")
if wiek >= 18:
    print("Możesz iść na prawo jazdy")
    print("Aha, ok...")
else:
    print("Jeszcze trochę brakuje...")
    print("Jeszcze",18 - wiek,"lat")
