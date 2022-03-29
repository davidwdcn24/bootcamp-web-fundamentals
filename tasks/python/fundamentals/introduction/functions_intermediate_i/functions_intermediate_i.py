# Variables
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'futbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

"""
1 Actualizar valores en diccionarios y listas

1.1. Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
1.2. Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
1.3. En el directorio_deportes, cambia "Messi" por "Andrés".
1.4. Cambia el valor 20 en z a 30.
"""
print("**********************INICIO (1)**********************")
def updateDictAndList() :
    # Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
    x[1][0] = 15
    
    # Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
    estudiantes[0]["last_name"] = "Bryant"
    
    # En el directorio_deportes, cambia "Messi" por "Andrés".
    directorio_deportes["futbol"][0] = "Andrés"
    
    # Cambia el valor 20 en z a 30.
    z[0]["y"] = 30
updateDictAndList()
print("Resultado de x:", x)
print("Resultado de estudiantes:", estudiantes)
print("Resultado de directorio_deportes:", directorio_deportes)
print("Resultado de z:", z)
print("**********************FIN (1)**********************")

"""
2 Iterar a través de una lista de diccionarios

Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, 
la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. 
Por ejemplo, dada la siguiente lista:

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary(estudiantes) 
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
print("**********************INICIO (2)**********************")
def iterateDictionary(some_list) :
    for itemList in some_list:
        resultado = []
        for itemKey in itemList.keys():
            resultado.append(itemKey + " - " + itemList[itemKey])
        print(", ".join(resultado))
iterateDictionary(estudiantes)
print("**********************FIN (2)**********************")

"""
3 Obtener valores de una lista de diccionarios

Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
la función imprima el valor almacenado en esa clave para cada diccionario. 
Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
Michael
John
Mark
KB

Y iterateDictionary2('last_name', estudiantes) debería generar:
Jordan
Rosales
Guillen
Tonel
"""
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
print("**********************INICIO (3)**********************")
def iterateDictionary2(key_name, some_list) :
    for itemList in some_list:
        print(itemList[key_name])
iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)
print("**********************FIN (3)**********************")

"""
4 Iterar a través de un diccionarios con valores de lista

Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, 
imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores 
asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# salida:
7 UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print("**********************INICIO (4)**********************")
def printInfo(some_dict) :
    for itemKey in some_dict.keys() :
        print(len(some_dict[itemKey]), itemKey.upper())
        for itemList in some_dict[itemKey] :
            print(itemList)
printInfo(dojo)
print("**********************FIN (4)**********************")