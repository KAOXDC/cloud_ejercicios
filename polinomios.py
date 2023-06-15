
############################################################################################## 
# Realiza un programa en Python que lea los numeros de tres fracciones, 
# la idea es que el programa permita sumar las fracciones y dar un resultado en fracciones
# Para sumar las tres fracciones debe hacerlo cno el metodo de encotrar el m.c.m.   
# Posteriormente complificar las fracciones y realizar la suma al final 
# Ejemplo:
# 
#  1     2     3
# --- + --- + ---
#  3     5     2
# 
# Hallamos el mcm de los denominadores
# 
#    3  5  2  | 2
#    3  5  1  | 3
#    1  5  1  | 5
#    1  1  1  | 
# 
# El  mcm es 2 * 3 * 5 = 30
# 
# luego complificamos/amplificamos multiplicando el denominador por un numero que este 
# incluido en los factores primos (2, 3, 5) y que nos de 30
# 
# Recordar que se multiplica por el mismo valor en el numerador y el denominador 
# 
#  1(10)      2(6)     3(15)
# ------  +  -----  +  -----
#  3(10)      5(6)     2(15)
# 
# 
#  10         12        45        10 + 12 + 45
# -----  +  -----  +  -----  =  ----------------  
#  30         30        30             30
# 
#                67   
# Solución  =   ----- 
#                30   
# 
# 
############################################################################################## 