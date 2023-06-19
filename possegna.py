# Importar string para la generación de letras al azar
import string
# Importar random para los cosos randomxd
import random

# Importar mis funcioncitas
from funcs import menu
from funcs import inputver as inv
from funcs import mrrobotto1 as rob


# Función para repetir el proceso hasta que el usuario quede satisfecho
def repeat():
    lenght, samples = menu.menu()

    contras = rob.genos(lenght, samples)
    print("Contraseñas generadas:")
    for i in range(len(contras)):
        print(''.join(x for x in contras[i]))
    
    print(f"\n\n ¿Estás conforme con estos resultados?")
    flag = inv.scanf(input(f"(-1 para salir, cualquier otro número para volver a generar) "))

    # Si no está conforme, regenerar
    if flag != -1:
        return repeat()



# Función Main
if __name__ == '__main__':

    # Presentaciónxd
    print(f"Hola, te doy la bienvenida a Possegna/Posseñña \n\n")

    # Interactuar con el buen usuario
    repeat()

