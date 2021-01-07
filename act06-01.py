
while True:
    print("ingrese un numero")
    numero = float(input(": "))

    if numero >= 0.001 and numero <=99999:
        if numero/10000 >=1 and numero/10000 < 10:
            print("la unidad más alta es decena de mil.")
        elif numero/1000 >=1 and numero/1000 < 10:
            print("la unidad más alta es Unidad de mil.")
        elif numero/100 >=1 and numero/100 < 10:
            print("la unidad más alta es Centena.")
        elif numero/10 >=1 and numero/10 < 10:
            print("la unidad más alta es Decena.")
        elif numero/1000 >=1 and numero/1000 < 10:
            print("la unidad más alta es Unidad.")
        elif numero*1000 >=1 and numero*1000 < 10:
            print("la unidad más alta es Milesima.")
        elif numero*100 >=1 and numero*100 < 10:
            print("la unidad más alta es Centesima.")
        elif numero*10 >=1 and numero*10 < 10:
            print("la unidad más alta es Decima.")
    else:
        print("numero invalido")

    print("========================\nDesea Continuar???, ingrese S/N: ")
    respuesta =input(": ")
    if respuesta.upper() == "N" or respuesta.upper() == "NO":
        break
