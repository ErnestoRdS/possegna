# Importar string para la generación de letras al azar
import string
# Importar random para los cosos randomxd
import random

# Importar mis funcioncitas
from funcs import menu


# Para generar las acás
def passÑÑa(lenght, samples):
    '''
        Generará varios ejemplos de contraseña
        Por el momento, lo único importante que se le pasa es un largo para la contraseña

        Atributos:
        lenght Int
        samples Int
    '''
    # Para guardar las contraseñas generadas
    contras = []
    for i in range(samples):
        temp = []
        # Iterar por el número de caracteres de longitud
        for char in range(lenght):
            temp.append(random.choice(string.ascii_letters))
        # Añadir la posible constraseña recién generada a la lista que regresaremos
        contras.append(temp)
    
    # Regresar los prospectos
    return contras


# Función Main
if __name__ == '__main__':

    # Presentaciónxd
    lenght, samples = menu.menu()

    contras = passÑÑa(lenght, samples)
    print("Contraseñas generadas:")
    for i in range(len(contras)):
        print(''.join(x for x in contras[i]))

