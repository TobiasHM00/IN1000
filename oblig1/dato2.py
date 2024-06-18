dato1 = int(input("Skriv en dato med måneden først (Eks: 1027): "))
dato2 = int(input("Skriv en dato med måneden først (Eks: 1131): "))

if dato1 > dato2:
    print("Feil rekkefølge!")
elif dato2 > dato1:
    print("Riktig rekkefølge!")
else:
    print("Samme dato!")
