print("**********************************************************")
print("1. Básico: imprime todos los números enteros del 0 al 150.")
print("**********************************************************")
# Le aumento el valor valor final a 151 para que se imprima también el 150.
for x in range(0, 151) :
    print(x)

print("************************************************************************")
print("2. Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.")
print("************************************************************************")
# Le aumento el valor valor final a 1001 para que se imprima también el 1000.
for x in range(5, 1001, 5) :
    print(x)

print("************************************************************************")
print("3. Contar, a la manera del Dojo: imprime números enteros del 1 " \
    "al 100. Si es divisible por 5, imprime 'Coding' en su lugar. Si es " \
    "divisible por 10, imprime 'Coding Dojo'.")
print("************************************************************************")
"""
Primero valida que seal múltiplo de 10.
Depués vaida si es múltiplo de 5.
"""
for x in range(1, 101) :
    if (x % 10 == 0) :
        print("Coding Dojo")
    elif (x % 5 == 0) :
        print("Coding")
    else :
        print(x)

print("************************************************************************")
print("4. Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000," \
    "e imprime la suma final.")
print("************************************************************************")
sum = 0
count = 0
# Imprime los números impares y los suma
while(count <= 500000) :
    if (count % 2 != 0) :
        sum += count;
        print(count)
    count += 1
print("suma: ", sum)

print("************************************************************************")
print("5. Cuenta regresiva de a 4: imprime números positivos comenzando desde el " \
    "2018, en cuenta regresiva de 4 en 4.")
print("************************************************************************")
count = 2018
while(count > 0):
    print(count)
    # resta 4 dígitos
    count -= 4

print("************************************************************************")
print("6. Contador flexible: establece tres variables: lowNum, highNum, mult. " \
    "Comenzando en lowNum y pasando por highNum, imprime solo los enteros que " \
    "sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El " \
    "bucle debe imprimir 3, 6, 9 (en líneas sucesivas).")
print("************************************************************************")
lowNum = 2
highNum = 9
mult = 3
# La variable mult debe ser diferente de 0
if (mult == 0) :
    mult = 1
for x in range(lowNum, highNum + 1) :
    if (x % mult == 0):
        print(x)