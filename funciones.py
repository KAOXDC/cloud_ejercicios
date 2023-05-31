
# x = 10
# # declarando una procedimieto saludar

# def saludar ():
# 	s = "HOLA"
# 	print (x)
# 	print ("Hola!") 

# # declarando una funcion despedir
# def despedir ():
# 	d = "CHAO"
# 	print (x)
# 	return d

# print(saludar())
# print(despedir())

# s = despedir()
# print (s)

# # funciones sin parametros 
# x = 123
# def sumar ():
# 	a = x
# 	b = -3
# 	return a + b

# def restar ():
# 	a = x
# 	b = 3
# 	return a - b

# print(sumar())
# print(restar())

# funciones con parametros 
# x = 123
def sumar (x, y):
	a = x
	b = y
	return a + b

def restar (x, y):
	a = x
	b = y
	return a - b

def multiplicar(x, y):
	return x * y

x = 3
y = 6
# print(sumar(x, y)) #9
# print(restar(x, y)) #-3
sumita = sumar(x, y) #9
restita = restar(x, y) #-3


# print(multiplicar(sumar(x, y), restar(x, y) )) # -27
print(multiplicar(sumita, restita )) # -27

