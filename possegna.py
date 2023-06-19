# Importar string para la generación de letras al azar
import string
# Importar random para los cosos randomxd
import random

# Importar mis funcioncitas
from funcs import menu
from funcs import mrrobotto1 as rob



# Función Main
if __name__ == '__main__':

    # Presentaciónxd
    lenght, samples = menu.menu()

    contras = rob.genos(lenght, samples)
    print("Contraseñas generadas:")
    for i in range(len(contras)):
        print(''.join(x for x in contras[i]))

