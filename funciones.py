
# # x = 10
# # # declarando una procedimieto saludar

# # def saludar ():
# # 	s = "HOLA"
# # 	print (x)
# # 	print ("Hola!") 

# # # declarando una funcion despedir
# # def despedir ():
# # 	d = "CHAO"
# # 	print (x)
# # 	return d

# # print(saludar())
# # print(despedir())

# # s = despedir()
# # print (s)

# # # funciones sin parametros 
# # x = 123
# def sumar ():
# 	a = float(input("ingres un número"))
# 	b = -3
# 	return a + b

# # def restar ():
# 	a = float(input("ingres un número"))
# # 	a = x
# # 	b = 3
# # 	return a - b

# # print(sumar())
# # print(restar())

# # funciones con parametros 
# # x = 123
# def sumar (x, y):
# 	a = x
# 	b = y
# 	return a + b

# def restar (x, y):
# 	a = x
# 	b = y
# 	return a - b

# def multiplicar(x, y):
# 	return x * y

# x = float(input("ingrese valor para x : "))
# y = 6
# # print(sumar(x, y)) #9
# # print(restar(x, y)) #-3
# sumita = sumar(x, y) #9
# restita = restar(x, y) #-3


# # print(multiplicar(sumar(x, y), restar(x, y) )) # -27
# print(multiplicar(sumita, restita )) # -27




# # placa = input("ingrese su placa : ")
# # placa = "HYP990"
# # placa = "HYP99D"

# # ultimo_digito = placa[5] 

# # validacion si no es numero es letra

# # in

# # ultimo_digito = placa[4] 

# # if ultimo_digito == 1 and ultimo_digito == 2:
# # 	print("tiene pico y placa el lunes")

# # print (ultimo_digito)


# # lunes = [9, 0]
# # martes = [1, 2]
# # miercoles = [3, 4]
# # jueves = [5, 6]
# # viernes = [7, 8]

# # dia = [lunes, martes, miercoles, jueves, viernes]
# # dia = [[9,0], [1,2], , , ],


# ############################### #
# Calcular el factorial de un numero ingresado
# por teclado, si el  factorial de un numero
# se  representa de la siguiente forma 
# n! = 1*2*3*4*5......(n-1)*n    
# Ejemplo 2: 4! =
# 1*2*3*4  = 24; 
# 4*3*2*1  = 24; 
# tenga en cuenta que el  factorial de 0! es 1   0! = 1 #
# aplicamos con funciones
# ############################### #

# declarar funcion para calcular el factorial  
def calcular_factorial (numero): # numero es la que almacena el numeropara calcular el factorial 
	factorial = 1
	for i in range(1, numero + 1, 1):
		factorial = factorial * i
	return factorial

# aplicacion principal 

n = int(input("ingrese un numero entero positivo "))
if n > 0: # evaluo si el numero ingresado es mayor que cero 
	final = calcular_factorial(n)
	print (final)
	# print (calcular_factorial(n))
elif n == 0:
	print ("El factorial de 0 es 1")
