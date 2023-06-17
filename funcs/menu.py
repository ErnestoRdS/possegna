# Función para verificar que el input esté bien, de lo contrario, volver a pedirlo
def verifyInput(input):
    if not input.isnumeric():
        return 'Pinche chistosito :)', False
    else:
        return input, True

# Función para br si la persona se va, o siguexd
def lifedecision():
    inp = input("Decisión turbo importante òwó (-1 ó 777): ")
    out, flag = verifyInput(inp)

    if not flag:
        print(out)
        return lifedecision()
    else:
        return inp, True


# Función para obtener la longitud
def getLenght():
    inp = input(f"¿Cuántos caracteres tiene que tener tu contraseña? ")
    out, flag = verifyInput(inp)

    if not flag:
        print(out)
        return lifedecision()
    else:
        return inp, True


# Función para obtener el número de ejemplos
def getSamples():
    inp = input(f"¿Cuántos ejemplos te gustaría recibir? ")
    out, flag = verifyInput(inp)

    if not flag:
        print(out)
        return lifedecision()
    else:
        return inp, True

# Función para presentar el programisha
def menu():
    print(f"Oal, bienvenido a Possegna/Posseñña \n\n")

    print(f"Si quieres salir, introduce un -1 (menos uno) \n")
    print(f"De lo contrario, ponle 777 (siete siete siete xd) y sigue las instrucciones para generar tu nueva contraseña uwu \n")

    out, _ = lifedecision()

    # Si introdujo -1, terminar el programa
    if out == -1:
        exit()
    
    # CONTINUAR
    # A tomar en cuenta
    lenght, _ = getLenght() # Largo
    lenght = int(lenght)
    samples, _ = getSamples() # Número de candidatos a contraseña a generar
    samples = int(samples)

    return lenght, samples
