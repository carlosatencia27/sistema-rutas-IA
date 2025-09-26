#!/usr/bin/env python3
import sys
import re
import heapq

# ================================
# 1. Funciones para cargar la base de conocimiento
# ================================
def cargar_base_conocimiento(archivo):
    estaciones = set()
    grafo = {}

    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("%"):
                continue

            if linea.startswith("station"):
                m = re.findall(r"station\(\s*([a-zA-Z0-9_]+)\s*\)", linea)
                if m:
                    estaciones.add(m[0])

            elif linea.startswith("edge"):
                m = re.findall(r"edge\(\s*([a-zA-Z0-9_]+)\s*,\s*([a-zA-Z0-9_]+)\s*,\s*cost\s*:\s*([0-9]+)\s*,\s*time\s*:\s*([0-9]+)\s*\)\s*\.", linea)
                if m:
                    origen, destino, costo, tiempo = m[0]
                    costo, tiempo = int(costo), int(tiempo)
                    grafo.setdefault(origen, []).append((destino, costo, tiempo))
                    grafo.setdefault(destino, []).append((origen, costo, tiempo))  # grafo no dirigido

    return estaciones, grafo

# ================================
# 2. Heurística y A*
# ================================
def heuristica(nodo, objetivo):
    # No tenemos coordenadas en kb.txt simple, devolvemos 0 -> A* = Dijkstra
    return 0

def a_estrella(grafo, inicio, fin, optimizar="cost"):
    # usamos prioridad basada en criterio pedido (cost, duration o mixed)
    # cada entrada: (f_priority, g_cost, g_time, nodo, ruta)
    heap = []
    heapq.heappush(heap, (0, 0, 0, inicio, []))
    visited = set()

    while heap:
        f, g_cost, g_time, nodo, ruta = heapq.heappop(heap)
        if (nodo, g_cost, g_time) in visited:
            continue
        ruta = ruta + [nodo]

        if nodo == fin:
            return ruta, g_cost, g_time

        visited.add((nodo, g_cost, g_time))

        for vecino, costo, tiempo in grafo.get(nodo, []):
            new_cost = g_cost + costo
            new_time = g_time + tiempo
            if optimizar == "cost":
                g_for_priority = new_cost
            elif optimizar == "duration":
                g_for_priority = new_time
            else:  # mixed
                g_for_priority = new_cost + new_time

            priority = g_for_priority + heuristica(vecino, fin)
            heapq.heappush(heap, (priority, new_cost, new_time, vecino, ruta))

    return None, float('inf'), float('inf')

# ================================
# 3. Main
# ================================
if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Uso: python route_finder.py kb.txt <origen> <destino> --optimize cost|duration|mixed")
        sys.exit(1)

    archivo_kb = sys.argv[1]
    origen = sys.argv[2]
    destino = sys.argv[3]

    if sys.argv[4] != "--optimize":
        print("Error: debes usar la opción --optimize")
        sys.exit(1)
    optimizar = sys.argv[5]

    estaciones, grafo = cargar_base_conocimiento(archivo_kb)
    if origen not in estaciones or destino not in estaciones:
        print(f"Error: las estaciones '{origen}' o '{destino}' no existen en la base de conocimiento.")
        sys.exit(1)

    ruta, total_cost, total_time = a_estrella(grafo, origen, destino, optimizar)
    if ruta:
        print(f"Ruta óptima encontrada: {' -> '.join(ruta)}")
        if optimizar == "cost":
            print(f"Costo total (cost): {total_cost}")
        elif optimizar == "duration":
            print(f"Tiempo total (duration): {total_time}")
        else:
            print(f"Costo total (mixed): {total_cost + total_time}")
    else:
        print("No se encontró ruta.")

