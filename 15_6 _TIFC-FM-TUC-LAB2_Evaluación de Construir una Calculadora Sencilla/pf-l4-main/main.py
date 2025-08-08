def sumar(a, b, c=None):
    """Suma dos o tres números y retorna el resultado."""
    if c is not None:
        return a + b + c
    return a + b

def restar(a, b, c=None):
    """Resta dos o tres números. Si son tres, resta b y c de a."""
    if c is not None:
        return a - b - c
    return a - b

def multiplicar(a, b, c=None):
    """Multiplica dos o tres números y retorna el resultado."""
    if c is not None:
        return a * b * c
    return a * b

def dividir(a, b, c=None):
    """Divide a entre b (y entre c si se proporciona)."""
    if b == 0 or (c is not None and c == 0):
        return "Error: No se puede dividir por cero."
    else:
        return a / b

def modulo(a, b, c=None):
    """Realiza la operación módulo entre a y b. No permite tres valores."""
    if c is not None:
        return "Error: Solo se permiten dos valores para módulo."
    if b == 0:
        return "Error: No se puede realizar módulo con cero."
    return a % b

def pedir_numeros(cantidad):
    #Solicita al usuario la cantidad de números indicada y los retorna como enteros.
    numeros = []
    for i in range(cantidad):
        num = float(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)
    return numeros

def main():
    #Función main() de la calculadora.
    while True:
        print("\nBienvenido a la Calculadora.")
        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Módulo")
        opcion = input("Seleccione la operación (1-5): ")
        if opcion not in ['1', '2', '3', '4', '5']:
            print("Opción inválida. Intente de nuevo.")
            continue
        cant = input("¿Cuántos valores desea usar? (2 o 3): ")
        if cant not in ['2', '3']:
            print("Cantidad inválida. Intente de nuevo.")
            continue
        cant = int(cant)
        nums = pedir_numeros(cant)
        if opcion == '1':
            resultado = sumar(*nums)
        elif opcion == '2':
            resultado = restar(*nums)
        elif opcion == '3':
            resultado = multiplicar(*nums)
        elif opcion == '4':
            resultado = dividir(*nums)
        elif opcion == '5':
            resultado = modulo(*nums)
        print(f"El resultado es: {resultado}")
        seguir = input("¿Desea realizar otra operación? (s/n): ").lower()
        if seguir != 's':
            print("¡Gracias por usar la calculadora!")
            break
main()



