#1
print("1", "Imprime en consola el valor 5")
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Imprime en consola el valor 5

#2
print("2", "Da un error porque no está definida la función number_of_days_in_a_week_silicon_or_triangle_sides")
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Da un error porque no está definida la función number_of_days_in_a_week_silicon_or_triangle_sides

#3
print("3", "Imprime en consola el valor 5")
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Imprime en consola el valor 5

#4
print("4", "Imprime en consola el valor 5")
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Imprime en consola el valor 5

#5
print("5", "Imprime en consola el valor 5 (llamada a la función) y luego imprime el valor por defecto None (valor de la variable x)")
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Imprime en consola el valor 5 (llamada a la función) y luego imprime el valor por defecto None (valor de la variable x)

#6
print("6", "Primero imprime el valor 3 (add(1,2)), luego imprime el valor 5 (add(2,3))"\
    " y al final da error porque la función no retorna valores. La función solo imprime valores en consola")
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))
# Primero imprime el valor 3 (add(1,2)), luego imprime el valor 5 (add(2,3))
# y al final da error porque la función no retorna valores. La función solo imprime valores en consola

#7
print("7", "Concatena los valores enviados (primero los transforma en string). En este ejemplo imprime en consola el valor 25")
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Concatena los valores enviados (primero los transforma en string). En este ejemplo imprime en consola el valor 25

#8
print("8", "Primero imprime en consola el valor 100. " \
    "Luego impime en consola el valor 10. ")
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Primero imprime en consola el valor 100. Luego impime en consola el valor 10.

#9
print("9", "Primero imprime en consola el valor 7. " \
    "Luego impime en consola el valor 14. " \
    "Luego impime en consola el valor 21. ")
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Primero imprime en consola el valor 7. Luego impime en consola el valor 14. Luego impime en consola el valor 21.

#10
print("10", "Imprime en consola el valor 8.")
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Imprime en consola el valor 8.

#11
print("11", "Primero imprime en consola el valor 500. " \
    "Luego imprime en consola el valor 500. " \
    "Luego imprime en consola el valor 300. " \
    "Luego imprime en consola el valor 500. ")
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# Primero imprime en consola el valor 500. Luego imprime en consola el valor 500. 
# Luego imprime en consola el valor 300. Luego imprime en consola el valor 500.

#12
print("12", "Primero imprime en consola el valor 500. " \
    "Luego imprime en consola el valor 500. " \
    "Luego imprime en consola el valor 300. " \
    "Luego imprime en consola el valor 500.")
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# Primero imprime en consola el valor 500. Luego imprime en consola el valor 500. 
# Luego imprime en consola el valor 300. Luego imprime en consola el valor 500.

#13
print("13", "Primero imprime en consola el valor 500. " \
    "Luego imprime en consola el valor 500. " \
    "Luego imprime en consola el valor 300. " \
    "Luego imprime en consola el valor 300.")
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# Primero imprime en consola el valor 500. Luego imprime en consola el valor 500. 
# Luego imprime en consola el valor 300. Luego imprime en consola el valor 300.

#14
print("14", "Primero imprime en consola el valor 1. " \
    "Luego imprime en consola el valor 3. " \
    "Luego imprime en consola el valor 2.")
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Primero imprime en consola el valor 1. Luego imprime en consola el valor 3. 
# Luego imprime en consola el valor 2.

#15
print("15", "Primero imprime en consola el valor 1. " \
    "Luego imprime en consola el valor 3. " \
    "Luego imprime en consola el valor 5. " \
    "Luego imprime en consola el valor 10.")
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# Primero imprime en consola el valor 1. Luego imprime en consola el valor 3. 
# Luego imprime en consola el valor 5. Luego imprime en consola el valor 10.