with open("analiza.txt",encoding="UTF-8") as plik:
    dane = plik.read()

nowy = ""

for x in dane:
    if x.isalpha() or x == " ":
        nowy = nowy + x

slowa = nowy.split()

wystapienia = {}
odrzucamy = [ "w", "i", "o", "a", "na", "to", "po", "te", "ale", "nie", "się" ]
for slowo in slowa:
    if slowo in odrzucamy:
        continue
    if slowo in wystapienia:
        wystapienia[slowo] += 1
    else:
        wystapienia[slowo] = 1
zw = 0
for slowo in wystapienia:
    lit = wystapienia[slowo]
    if lit > 5:
        print("Słowo",slowo,"Występuje",lit)
        if lit > zw:
            zw = lit
            wygrany = slowo + str(lit)

print("---------")
print("Wygrywa:", wygrany)
