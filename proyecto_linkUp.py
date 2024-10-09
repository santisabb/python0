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
user_name = input("Ingrese su nombre: ")
anio_actual = 2024
user_birth_year = input("Ingrese su año de nacimiento: ")
int_year = int(user_birth_year)
user_age = anio_actual - int_year
user_city = input("Por ultimo ingrese en que ciudad reside actualmente:")
os.system('cls' if os.name == 'nt' else 'clear')
print("Perfecto! ya ingresaste todos tus datos, aquí te va una vista de tu perfil")
print('--------------------------------------------------------------------------------')
print('Nombre: ' + user_name)
print('Edad: ' + str(user_age))
print('Ciudad de residencia: ' + user_city)