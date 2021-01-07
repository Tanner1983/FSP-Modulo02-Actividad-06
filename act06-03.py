#•	Calcular las notas (3) obtenidas durante el semestre.
#•	Mostrar la categoría, promedio alcanzado y % de beca logrado.
#•	Señalar la aprobación o no del ramo.
def imprimir(promedio, categoria, beca):
    print("\n======= Información ========\n")
    print(f"El promedio de notas es {promedio},\nesta en la categoria de {categoria},\ny tiene acceso a una beca del {beca}\n")

while True:
    
    print("Ingrese 3 notas")
    nota1= float(input(": "))
    nota2= float(input(": "))
    nota3= float(input(": "))
    
    if nota1 <=0 or nota1 >= 71:
        print("La nota N°1 es invalida")
    elif nota2 <=0 or nota1 >= 71:
        print("La nota N°2 es invalida")
    elif nota3 <=0 or nota1 >= 71:
        print("La nota N°3 es invalida")    
    else:    
        promedio= float(nota1 + nota2 + nota3)/3        

        if promedio >=65 and promedio <= 70 or promedio >=6.5 and promedio <= 7.0: 
            categoria="Excelencia"
        elif promedio >=55 and promedio <= 64 or promedio >=5.5 and promedio <= 6.4:
            categoria="Muy Bueno"
        elif promedio >=40 and promedio <= 54 or promedio >=4.0 and promedio <= 5.4:
            categoria="Bueno"
        elif promedio >=30 and promedio <= 39 or promedio >=3.0 and promedio <= 3.9:
            categoria="Malo"
        else:
            categoria="Deficiente"

        if promedio >=68 and promedio <=70 or promedio >=6.8 and promedio <=7.0:
            beca="100%"
        elif promedio >=65 and promedio <=67 or promedio >=6.5 and promedio <=6.7:
            beca="90%"
        elif promedio >=60 and promedio <=64 or promedio >=6.0 and promedio <=6.4:
            beca="80%"
        elif promedio >=55 and promedio <=59 or promedio >=5.5 and promedio <=5.9:
            beca="50%"
        else:
            beca="0%"        

        imprimir(promedio, categoria, beca)

    respuesta = input("Desea ingresar mas notas SI/NO: ")
    if respuesta.upper()=="NO" or respuesta.upper()=="N":
        break
