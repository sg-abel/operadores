#Exercise 1
age = 35
print(age)
height = float(1.68)
print(height)
complex_number = (1 + 1j)
print(complex_number)
#area de un tringulo
base = 20
height = 10
area_del_triangulo = int(0.5 * base * height)
print('El area del triangulo es: ', area_del_triangulo)
#perimetro del traingulo
a = 5
b = 4
c = 3
perimetro_del_triangulo = (a + b + c)
print('El perimetro del triangulo es: ', perimetro_del_triangulo)
#area del rectangulo
length = 6
width = 3
area_del_rectangulo = 2 * length * width
print('El area del rectangulo es:', area_del_rectangulo)
#radio de un circulo 
pi = 3.14
radio = 15
area_del_circulo = pi * radio ** 2
print('El area del ciruclo es:', area_del_circulo)
#circunferencia del circulo
circunferencia = 2 * pi * radio
print('La circunferencia es:', circunferencia)
#calcula la pendiente x-inter y y-inter de y=2x-2
m_1 = 2 #pendiente
x = 2
y = 2*2-2
print(m_1)
print(y)
#Pendiente de un eclipse m = 2y-y1/x2-x1 (2,2)(6,10)
x_inter = 6-2
y_inter = 10-2
m_2 = x_inter / y_inter
print(m_2)
#comparacion de pendientes
print(m_1 == m_2)
x= -1
y= (x^2)+(6*x)+9
print(y)
print(len('python') != len('dragon'))
print(('python' in 'dragon') and ('dragon' in 'python'))
#jerga en la oracion
print('Espero que este curso no este lleno de jerga,', 'jerga' in 'Espero que este curso no este lleno de jerga')
#letras de python en float y convertirlo en string
text = 'python'
num_len = len('python')
print(text)
print('la longitu es:',len(text))
print('en numero flotante:', float(num_len))
print("en String es:", str(num_len))
#comprobando si un numero es par
#si 2 / 2 es numero par es Verdad
par = (0,2,4,6,8,10,12)
print( (40/ 2) in par)
#comprobaciones
print(7//3 == int(2.7))
print("10" is 10)
print(int(9.8) == 10)
#calcula el salario de una persona
horas_de_trabajo = int(input('cuantas horas trabajas?:'))
pago_por_hora = int(input('cuanto ganas por hora?:'))
pago_por_semana = horas_de_trabajo * pago_por_hora
print("tu ganas por semana:", pago_por_semana)
#calculando tu edad en segundos
edad = int(input('Escribe tu edad:'))
segundos = 31536000
edad_en_seg = edad * segundos
print("tu edad en segundos es:", edad_en_seg, 'segundos')
#script que muestra una lista
print(1, 1, 1, 1, 1)
def secuencia_potencias(n):
    """
    Genera la secuencia de potencias para un número dado n.
    
    Args:
        n (int): Número de fila
    
    Returns:
        list: Secuencia de potencias [1, n, n^2, n^3, n^4]
    """
    return [n**i for i in range(5)]

# Ejemplo de uso
for i in range(1, 6):
    print(secuencia_potencias(i))



