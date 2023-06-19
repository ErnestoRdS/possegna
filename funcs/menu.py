# Importar funciones de verifiers.py
from . import inputver as inv


# Función para presentar el programisha
def menu():

    print(f"Sigue las instrucciones para generar tu nueva contraseña \n")
    print(f"Si quieres salir, puedes introducir -1 (menos uno) en cualquier momento \n")

    print(f"¿Cuántos caracteres debe tener tu contraseña? ")
    lenght = inv.scanf(input()) # Largo
    print(f"¿Cuántos prospectos quieres ver? ")
    samples = inv.scanf(input()) # Número de candidatos a contraseña a generar
    samples = int(samples)

    return lenght, samples
