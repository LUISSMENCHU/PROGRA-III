from bst import BST
from graphviz_export import export_to_graphviz
from utils import load_from_file

def main():
    bst = BST()
    while True:
        print("\n--- MENÚ ABB ---")
        print("1. Insertar número")
        print("2. Buscar número")
        print("3. Eliminar número")
        print("4. Cargar desde archivo")
        print("5. Exportar a Graphviz")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            num = int(input("Ingrese número a insertar: "))
            bst.insert(num)
            print("Número insertado.")
        elif opcion == "2":
            num = int(input("Ingrese número a buscar: "))
            nodo = bst.search(num)
            print("Número encontrado." if nodo else "Número no encontrado.")
        elif opcion == "3":
            num = int(input("Ingrese número a eliminar: "))
            bst.delete(num)
            print("Número eliminado.")
        elif opcion == "4":
            path = input("Ingrese ruta del archivo .txt: ")
            load_from_file(bst, path)
        elif opcion == "5":
            export_to_graphviz(bst.root)
            print("Archivo 'abb.dot' generado.")
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
