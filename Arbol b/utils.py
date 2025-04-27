
import csv
from graphviz import Digraph

def cargar_csv(ruta):
    claves = []
    with open(ruta, newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            for valor in fila:
                if valor.strip().isdigit():
                    claves.append(int(valor))
    return claves

def exportar_grafico(arbol, nombre="arbol_b"):
    dot = arbol.to_graphviz()
    dot.render(nombre, view=True)
