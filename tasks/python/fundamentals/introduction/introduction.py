import random

"""
print(type(24))
print(type(3.9))
print(type(3j))
print(1 + 3j)
"""

"""
int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))
"""


print(random.randint(2,5))

# Cadenas
name = "Zen"
print("Mi nombre es", name)

name = "CoodingDojo"
print("Mi nombre es " + name)

#print("Hola" + 42)
print("Hola" + str(42))

total = 35
user_val = "26"
#total = total + user_val
total = total + int(user_val)


first_name = "Zen"
last_name = "Coder"
age = 27
print(f"Mi nombre is {first_name} {last_name} and tengo {age} años de edad.")

first_name = "Zen"
last_name = "Coder"
age = 27
print("Mi nombre es {} {} y tengo {} años de edad.".format(first_name, last_name, age))
# salida: Mi nombres es Zen Coder y tengo 27 años de edad.
print("Mi nombre es {} {} y tengo {} años de edad.".format(age, first_name, last_name))
# salida: Mi nombre es 27 Zen y tengo Coder años de edad.


hw = "Hola %s" % "mundo" 	# con valores literales
py = "Me encanta Python %d" % 3 
print(hw, py)
# salida: Hola mundo Me encanta Python 3
name = "Zen"
age = 27
print("Mi nombre es %s y tengo %d" % (name, age))		# o con variables
# salida: Mi nombre es Zen y tengo 27

x = "hola mundo"
print(x.title())

print("########### listas #########")


frutas = ['manzana', 'plátano', 'naranja', 'frutilla']
vegetales = ['lechuga', 'pepino', 'zanahorias']
frutas_y_vegetales = frutas + vegetales
print(frutas_y_vegetales)
ensalada = 3 * vegetales
print(ensalada)


x = [1,2,3,4,5]
x.append(99)
print(x)

x = [99,4,2,5,-3]
print(x[:])
# la salida sería [99,4,2,5,-3]
print(x[1:])
# la salida sería [4,2,5,-3];
print(x[:4])
# la salida sería [99,4,2,5]
print(x[2:4])
# la salida sería [2,5];

x=[5,34,10,1,6]
x += [2]
print(x)

x = [];
if not x :
    print("lista vacia")
else :
    print("algo")
