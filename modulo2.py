resultado = ""
distancia = 0.01
tiempo = 1
dist_metros = distancia * 1000
tiempo_horas = tiempo / 3600
vel_ms = dist_metros / tiempo
vel_km = distancia / tiempo_horas
resultado = "La velocidad es de " + str(vel_km) + "km/h o de " + str(vel_ms) + "m/s"
print(resultado)
xor = False
a = True
b = True
xor = a == b
print(xor)