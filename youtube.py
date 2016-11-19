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

# ---------------------------------------------------------------------

def main():
    url_link = input('\nIntroduzca una URL de youtube: ')
    loop = input('\n¿Cuantas veces quieres que se repita? ')
    loop = int(loop)
    porcentaje = 100/loop
    porcentaje_2 = porcentaje
    print('\nProgreso:')
    for i in range(loop):
        webbrowser.Mozilla
        webbrowser.Chrome
        print('\r',porcentaje, '%')
        porcentaje = porcentaje + porcentaje_2
        webbrowser.open(url_link, new=1, autoraise=True)

        time.sleep(5)
# Programa principal
# ---------

print('\n ¡¡Bienvenido al script para Youtube @ Barea13!!')
main()
