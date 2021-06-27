liczba = int(input("liczba: "))
iloczyn = 1
while liczba > 0:
    cyfra = liczba % 10
    iloczyn = iloczyn * cyfra
    print("cyfra:", cyfra)
    print("il:",iloczyn)
    liczba = liczba // 10

print(iloczyn)
