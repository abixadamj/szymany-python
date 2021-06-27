liczba = int(input("liczba: "))
while liczba > 0:
    cyfra = liczba % 10
    print("cyfra:", cyfra)
    liczba = liczba // 10
