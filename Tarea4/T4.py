# avl_tree.py
import csv
from graphviz import Digraph

class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class ABB:
    def insertar(self, raiz, clave):
        if not raiz:
            return Nodo(clave)
        elif clave < raiz.clave:
            raiz.izquierda = self.insertar(raiz.izquierda, clave)
        else:
            raiz.derecha = self.insertar(raiz.derecha, clave)
        return raiz

    def buscar(self, raiz, clave):
        if not raiz or raiz.clave == clave:
            return raiz
        if clave < raiz.clave:
            return self.buscar(raiz.izquierda, clave)
        return self.buscar(raiz.derecha, clave)

    def eliminar(self, raiz, clave):
        if not raiz:
            return raiz
        if clave < raiz.clave:
            raiz.izquierda = self.eliminar(raiz.izquierda, clave)
        elif clave > raiz.clave:
            raiz.derecha = self.eliminar(raiz.derecha, clave)
        else:
            if not raiz.izquierda:
                return raiz.derecha
            elif not raiz.derecha:
                return raiz.izquierda
            temp = self.min_valor_nodo(raiz.derecha)
            raiz.clave = temp.clave
            raiz.derecha = self.eliminar(raiz.derecha, temp.clave)
        return raiz

    def min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual

class AVL(ABB):
    def insertar(self, raiz, clave):
        raiz = super().insertar(raiz, clave)
        return self._balancear(raiz, clave)

    def eliminar(self, raiz, clave):
        raiz = super().eliminar(raiz, clave)
        if not raiz:
            return raiz
        raiz.altura = 1 + max(self._altura(raiz.izquierda), self._altura(raiz.derecha))
        balance = self._obtener_balance(raiz)

        if balance > 1 and self._obtener_balance(raiz.izquierda) >= 0:
            return self._rotacion_derecha(raiz)
        if balance < -1 and self._obtener_balance(raiz.derecha) <= 0:
            return self._rotacion_izquierda(raiz)
        if balance > 1 and self._obtener_balance(raiz.izquierda) < 0:
            raiz.izquierda = self._rotacion_izquierda(raiz.izquierda)
            return self._rotacion_derecha(raiz)
        if balance < -1 and self._obtener_balance(raiz.derecha) > 0:
            raiz.derecha = self._rotacion_derecha(raiz.derecha)
            return self._rotacion_izquierda(raiz)
        return raiz

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _obtener_balance(self, nodo):
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha) if nodo else 0

    def _balancear(self, nodo, clave):
        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        balance = self._obtener_balance(nodo)

        if balance > 1 and clave < nodo.izquierda.clave:
            return self._rotacion_derecha(nodo)
        if balance < -1 and clave > nodo.derecha.clave:
            return self._rotacion_izquierda(nodo)
        if balance > 1 and clave > nodo.izquierda.clave:
            nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)
        if balance < -1 and clave < nodo.derecha.clave:
            nodo.derecha = self._rotacion_derecha(nodo.derecha)
            return self._rotacion_izquierda(nodo)

        return nodo

    def _rotacion_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda
        y.izquierda = z
        z.derecha = T2
        z.altura = 1 + max(self._altura(z.izquierda), self._altura(z.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        return y

    def _rotacion_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha
        y.derecha = z
        z.izquierda = T3
        z.altura = 1 + max(self._altura(z.izquierda), self._altura(z.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        return y

    def cargar_desde_csv(self, ruta):
        raiz = None
        with open(ruta, newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                for valor in fila:
                    if valor.strip().isdigit():
                        raiz = self.insertar(raiz, int(valor.strip()))
        return raiz

    def graficar(self, raiz, nombre_archivo="arbol_avl"):
        dot = Digraph()

        def agregar_nodos(nodo):
            if nodo:
                dot.node(str(id(nodo)), str(nodo.clave))
                if nodo.izquierda:
                    dot.edge(str(id(nodo)), str(id(nodo.izquierda)))
                    agregar_nodos(nodo.izquierda)
                if nodo.derecha:
                    dot.edge(str(id(nodo)), str(id(nodo.derecha)))
                    agregar_nodos(nodo.derecha)

        agregar_nodos(raiz)
        dot.render(nombre_archivo, format='png', cleanup=True)

if __name__ == "__main__":
    arbol = AVL()
    raiz = None

    while True:
        print("\n--- Menú AVL ---")
        print("1. Insertar número")
        print("2. Buscar número")
        print("3. Eliminar número")
        print("4. Cargar desde CSV")
        print("5. Visualizar con Graphviz")
        print("6. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            num = int(input("Ingrese número a insertar: "))
            raiz = arbol.insertar(raiz, num)
        elif opcion == "2":
            num = int(input("Ingrese número a buscar: "))
            resultado = arbol.buscar(raiz, num)
            print("Encontrado" if resultado else "No encontrado")
        elif opcion == "3":
            num = int(input("Ingrese número a eliminar: "))
            raiz = arbol.eliminar(raiz, num)
        elif opcion == "4":
            archivo = input("Ingrese nombre de archivo CSV: ")
            raiz = arbol.cargar_desde_csv(archivo)
            print("Datos cargados desde", archivo)
        elif opcion == "5":
            arbol.graficar(raiz)
            print("Árbol visualizado como 'arbol_avl.png'")
        elif opcion == "6":
            break
        else:
            print("Opción inválida")
