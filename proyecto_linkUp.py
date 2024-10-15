import os

print("Bienvenido a...")
print("""
ooooo         o8o              oooo        ooooo     ooo            
`888'         `"'              `888        `888'     `8'            
 888         oooo  ooo. .oo.    888  oooo   888       8  oo.ooooo.  
 888         `888  `888P"Y88b   888 .8P'    888       8   888' `88b 
 888          888   888   888   888888.     888       8   888   888 
 888       o  888   888   888   888 `88b.   `88.    .8'   888   888 
o888ooooood8 o888o o888o o888o o888o o888o    `YbodP'     888bod8P' 
                                                          888       
                                                         o888o                                                                     
""")
#EJERCICIO 1: solicitar datos al usuario, como edad, país, direccion, nombre completo, etc.
# user_name = input("Ingrese su nombre: ")
# anio_actual = 2024
# user_birth_year = input("Ingrese su año de nacimiento: ")
# int_year = int(user_birth_year)
# user_age = anio_actual - int_year
# user_city = input("Por ultimo ingrese en que ciudad reside actualmente:")
# os.system('cls' if os.name == 'nt' else 'clear')
# print("Perfecto! ya ingresaste todos tus datos, aquí te va una vista de tu perfil")
# print('--------------------------------------------------------------------------------')
# print('Nombre: ' + user_name)
# print('Edad: ' + str(user_age))
# print('Ciudad de residencia: ' + user_city)

#EJERCICIO 2: Permitir al usuario decidir si quiere escribir un mensaje
# d = input('Desea escribir un mensaje para su perfil publico?(S/N)')
# while d != 'N' and d != 'n':
#     user_message = input('Ingrese su mensaje:')
#     d = input('Desea escribir otro mensaje?(S/N)')

#EJERCICIO 3: Desarrollar un menu de opciones que le permita al usuario
#elegir una opcion y/o salir del programa
opc = -1
while opc != 0:
    print('--------------------------------------------')
    print('MENU DE OPCIONES')
    print('--------------------------------------------')
    print('1- Ingresar datos de usuario')
    print('2- Publicar un mensaje')
    print('3- Mostrar datos del usuario')
    print('0- Salir')
    opc = int(input('Ingrese una opcion(0 significa salir)'))
    if opc == 1:
        user_name = input("Ingrese su nombre: ")
        anio_actual = 2024
        user_birth_year = input("Ingrese su año de nacimiento: ")
        int_year = int(user_birth_year)
        user_age = anio_actual - int_year
        user_city = input("Por ultimo ingrese en que ciudad reside actualmente:")
        os.system('cls' if os.name == 'nt' else 'clear')
    if opc == 2:
        user_message = input('Ingrese su mensaje:')
        os.system('cls' if os.name == 'nt' else 'clear')
    elif opc == 3:
        print('Nombre: ' + user_name)
        print('Edad: ' + str(user_age))
        print('Ciudad de residencia: ' + user_city)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif opc == 0:
        print('Nos vemos la proxima rey')

