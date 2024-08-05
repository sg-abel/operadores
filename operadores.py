#Booleam
print(True)
print(False)
#operadares
print('addition: ', 1 + 2) #3
print('Substraccion: ', 2 - 1)
print('multiplicacion: ', 2 * 4)
print('division: ', 8 / 2)
print('division: ', 7 / 2)
print('Exponencial: ', 2 ** 3)
#float
print('floating Ponit Number, PI', 3.14)
print('Floating Ponit Number, gravity', 9,81)
#Numeros complejos
print('Complex number: ', 1 + 1j)
print('multiplying complex number: ', (1 + 1j)*(1 - 1j))
#declaracion de variables
a = 3
b = 2
#operaciones aritmeticas y asignacion a la variable
total = a + b
diff = a - b
multi = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b
print('a:',a ,'b:', b)
print('a + b: ', total)
print('a - b: ', diff)
print('a * b: ', multi)
print('a / b: ', division)
print('a ** b: ', exponential)
#calculando el area de un circulo
radio = 10
area_del_circulo = 3.14 * radio * 2
print('Area del circulo:',area_del_circulo)
print(int(area_del_circulo))
#calculando el area de un rectangulo
length = 75
width = 20
area_del_rectangulo = length * width
print('Area del rectangulo:', area_del_rectangulo)
#calculando el peso de un objeto
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight,'N') #Agregando la unidad del peso
#calculando la densidad de un liquido
mass = 75 #en kilos
volume = 0.075 #en metros cubicos
density = mass / volume # 1000 kg/m^3
print(density)
#comparacion de operadores
# == igual
# != no igual
# > mayor que
# < menor que
# >= mayor igual que
# <= menor igual que
print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 < 3)
print(3 <= 2)
print(3 == 2)
print(3 != 2)
print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print('False == False: ', False == False)
#ademas en Python se usa como comparacion is, is not, in, not in
print(' 1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)
print('A in Abel', 'A' in 'Abel')
print('B in Abel', 'B' in 'Abel')
print('b in Abel', 'b' in 'Abel')
#operadores logicos
print(3 > 2 and 4 > 3)
print(3 > 2 and 4 < 3)
print(3 > 2 or 4 > 3)
print(not 3 > 2)
print(not 3 < 2)




