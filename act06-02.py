#Se pide:
#•	Solicitar el total de los ingresos del hogar.
#•	Solicitar la cantidad de personas que habitan el hogar.
#•	Mostrar el percentil asociado a su ingreso.

def imprimir(ingresos, ingresoX,decil):
    print("\n========== Informe ==========\n")
    print(f"Segun sus ingresos totales ${ingresos}\ntiene un ingreso por persona que asciende a ${ingresoX}\nUd. corresponde al {decil}\n")
    return

print("Ingrese el total de los ingresos del hogar")
ingresos=int(input(": "))
print("------------------------------------------")
print("Ingrese la cantidad de integrantes que viven en su hogar")
nPersonas=int(input(": "))
print("------------------------------------------")

ingresoX= ingresos/nPersonas
if ingresoX >= 0 and ingresoX <= 48750:
    decil= "1° decil"
elif ingresoX >= 48751 and ingresoX <= 74969:
    decil= "2° decil"
elif ingresoX >= 74970 and ingresoX <= 100709:
    decil= "3° decil"
elif ingresoX >= 100710 and ingresoX <= 125558:
    decil= "4° decil"
elif ingresoX >= 125559 and ingresoX <= 154166:
    decil= "5° decil"
elif ingresoX >= 154167 and ingresoX <= 193104:
    decil= "6° decil"
elif ingresoX >= 193105 and ingresoX <= 250663:
    decil= "7° decil"
elif ingresoX >= 250664 and ingresoX <= 352743:
    decil= "8° decil"
elif ingresoX >= 352744 and ingresoX <= 611728:
    decil= "9° decil"
else:
    decil= "10° decil"

imprimir(ingresos, ingresoX, decil)
