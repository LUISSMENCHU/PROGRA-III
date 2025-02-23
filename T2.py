def convertir_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return convertir_a_binario(n // 2) + str(n % 2)


def contar_digitos(n):
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)


def calcular_raiz_cuadrada(n, i=1):
    if i * i > n:
        return i - 1
    return calcular_raiz_cuadrada(n, i + 1)


def raiz_cuadrada_entera(n):
    return calcular_raiz_cuadrada(n)


def valores_romanos():
    return {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def convertir_a_decimal(romano, valores=None):
    if valores is None:
        valores = valores_romanos()
    if len(romano) == 1:
        return valores[romano]
    if valores[romano[0]] < valores[romano[1]]:
        return -valores[romano[0]] + convertir_a_decimal(romano[1:], valores)
    return valores[romano[0]] + convertir_a_decimal(romano[1:], valores)


def suma_numeros_enteros(n):
    if n == 0:
        return 0
    return n + suma_numeros_enteros(n - 1)


def menu():
    while True:
        print("\nMenú:")
        print("1. Convertir a Binario")
        print("2. Contar Dígitos")
        print("3. Raíz Cuadrada Entera")
        print("4. Convertir a Decimal desde Romano")
        print("5. Suma de Números Enteros")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            num = int(input("Ingrese un número entero: "))
            print("Binario:", convertir_a_binario(num))
        elif opcion == '2':
            num = int(input("Ingrese un número entero: "))
            print("Cantidad de dígitos:", contar_digitos(num))
        elif opcion == '3':
            num = int(input("Ingrese un número entero: "))
            print("Raíz cuadrada entera:", raiz_cuadrada_entera(num))
        elif opcion == '4':
            romano = input("Ingrese un número romano: ").upper()
            print("Decimal:", convertir_a_decimal(romano))
        elif opcion == '5':
            num = int(input("Ingrese un número entero positivo: "))
            print("Suma de números enteros:", suma_numeros_enteros(num))
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
