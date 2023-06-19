# Importar string para la generación de letras al azar
import string as str
# Importar random
import random as rnd

# Para generar las contraseñas
def genos(lenght, samples):

    # Tomar los caracteres para la contraseña del siguiente conjuntod de caracteres
    chars = str.ascii_letters + str.digits + str.punctuation
    # Para guardar las contraseñas generadas
    contras = []

    for i in range(samples):
        temp = ""
        # Iterar por el número de caracteres de longitud
        for _ in range(lenght):
            temp += rnd.choice(chars)
        # Añadir la posible constraseña recién generada a la lista que regresaremos
        contras.append(temp)
    
    # Regresar los prospectos
    return contras