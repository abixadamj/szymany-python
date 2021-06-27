# funkcja liczy średnią z listy
# [ 1,3,5,7,43,23,22 ] - średnia

def srednia(liczby):
    koszyk = 0
    elementow = len(liczby)
    print(koszyk,elementow,liczby)
    for x in range(elementow):
        koszyk += liczby[x]
    print(koszyk,elementow,liczby)
    srednia = koszyk / elementow
    print("s=",srednia,"u:",koszyk)

def sredniap(liczby):
    s = sum(liczby)
    print("śr",s/len(liczby),"sum:",s)
