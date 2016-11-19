#! /usr/bin/python
# -*- coding: utf-8 -*-
# Barea's Code

# Módulos
import webbrowser
import time
# Constantes

# Clases
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
def looping(loop, tiempo, porcentaje, porcentaje_2, url_link):
    for i in range(loop):
        webbrowser.Mozilla
        webbrowser.Chrome
        print('\r',porcentaje, '%')
        porcentaje = porcentaje + porcentaje_2
        webbrowser.open(url_link, new=1, autoraise=True)

        time.sleep(tiempo)
# ---------------------------------------------------------------------

def main():
    url_link = input('\nIntroduzca una URL de youtube: ')
    loop = input('\n¿Cuantas veces quieres que se repita? ')
    loop = int(loop)
    tiempo = input('\nIntervalo de tiempo entre URL y URL (en segundos): ')
    tiempo = int(tiempo)
    porcentaje = 100/loop
    porcentaje_2 = porcentaje
    print('\nProgreso:')
    looping(loop, tiempo, porcentaje, porcentaje_2, url_link)
    print('Terminado con éxito!! El script se cerrará en 5 segundos...')
    time.sleep(5)
# Programa principal
# ---------

print('\n ¡¡Bienvenido al script para Youtube @ Barea13!!')
main()
