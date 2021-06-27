ile = 0
for x in range(1,101):
    if x % 5 == 0:
        print("5:",x)
        ile = ile + 1
    if x % 3 == 0:
        print("3:",x)
        
print("liczb jest",ile)
