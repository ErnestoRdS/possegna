# Función para verificar que el input esté bien, de lo contrario, volver a pedirlo
def verifyInput(input):
    if int(input) == -1:
        print("Bye-bye, cuídate")
        exit()
    if not input.isnumeric():
        print(f"Introduce un valor correcto, por favor ")
        return input, False
    else:
        return input, True
    

# Función para obtener la longitud
def scanf(input):
    out, flag = verifyInput(input)

    if not flag:
        print(out)
        return scanf(input)
    else:
        return int(out)
