# Función para verificar que el input esté bien, de lo contrario, volver a pedirlo
def verifyInput(input):
    if not input.isnumeric():
        print(f"Introduce un valor correcto, por favor ")
        return input, False
    else:
        return input, True
    

# Función para obtener la longitud
def scanf(input):
    out, flag = verifyInput(input)

    if int(out) == -1:
        exit()
    if not flag:
        print(out)
        return scanf(input)
    else:
        return int(out)
