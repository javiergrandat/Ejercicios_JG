import time

tiempo_inicial = time.time()

objetivo = int(input('Escoge un numero: '))
epsilon = 0.0001
paso = epsilon**2 
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cudrada de {objetivo} es {respuesta}')

tiempo_final = time.time()

print(f'El tiempo de ejecucion fue de {tiempo_final - tiempo_inicial}')