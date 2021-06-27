# program badający, czy liczba jest pierwsza i ile ich jest

pierwsze = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
            41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
            89, 97, 101, 103, 107, 109, 113]

# zakres od 1 do...
koncowa = int(input("Podaj liczbę końcową: "))
ile_liczb = 0

if koncowa < 114:

    for i in range(0, koncowa+1):
        print("Sprawdzam liczbę:",i)
        if i in pierwsze:
            print("To jest liczba pierwsza")
            ile_liczb = ile_liczb + 1
    print("W zakresie jest", ile_liczb,"liczb pierwszych.")
    
else:
    print("Trochę za duża liczba.. max. 113")


