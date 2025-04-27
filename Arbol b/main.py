
from arbol_b import BTree
from utils import cargar_csv, exportar_grafico

def menu():
    grado = int(input("Ingrese el grado del Árbol B: "))
    arbol = BTree(grado)
    
    while True:
        print("\n1. Insertar clave\n2. Buscar clave\n3. Eliminar clave (no implementado)\n4. Cargar CSV\n5. Mostrar gráfico\n6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            clave = int(input("Ingrese la clave: "))
            arbol.insert(clave)
        elif opcion == "2":
            clave = int(input("Clave a buscar: "))
            print("Encontrado" if arbol.search(clave) else "No encontrado")
        elif opcion == "3":
            print("Eliminación no implementada aún.")
        elif opcion == "4":
            path = input("Ruta del archivo CSV: ")
            claves = cargar_csv(path)
            for clave in claves:
                arbol.insert(clave)
        elif opcion == "5":
            exportar_grafico(arbol)
        elif opcion == "6":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
