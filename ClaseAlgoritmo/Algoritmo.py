class Algoritmo:
    def __init__(self, datos=None):
            self.datos = datos

    def busqueda_lineal(self, elemento):
            for i in range(len(self.datos)):
                 if self.datos[i] == elemento:
                    return i
            return -1

    def busqueda_binaria(self, elemento):
        return self.divide_y_venceras(elemento)

    def divide_y_venceras(self, elemento):
        datos_ordenados = sorted(self.datos)
        izquierda = 0
        derecha = len(datos_ordenados) - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if datos_ordenados[medio] == elemento:
                return datos_ordenados.index(elemento)
            elif datos_ordenados[medio] < elemento:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return -1

    def heap_sort(self):
        datos = self.datos.copy()
        n = len(datos)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(datos, i, n)

        for i in range(n - 1, 0, -1):
            datos[0], datos[i] = datos[i], datos[0]
            self._heapify(datos, 0, i)

        return datos

    def _heapify(self, datos, i, n):
        izquierda = 2 * i + 1
        derecha = 2 * i + 2
        mayor = i

        if izquierda < n and datos[izquierda] > datos[mayor]:
            mayor = izquierda

        if derecha < n and datos[derecha] > datos[mayor]:
            mayor = derecha

        if mayor != i:
            datos[i], datos[mayor] = datos[mayor], datos[i]
            self._heapify(datos, mayor, n)

    def merge_sort(self):
        datos = self.datos.copy()
        if len(datos) > 1:
            medio = len(datos) // 2
            izquierda = datos[:medio]
            derecha = datos[medio:]

            izquierda = self._merge_sort(izquierda)
            derecha = self._merge_sort(derecha)

            return self._merge(izquierda, derecha)
        return datos

    def _merge_sort(self, datos):
        if len(datos) > 1:
            medio = len(datos) // 2
            izquierda = datos[:medio]
            derecha = datos[medio:]

            izquierda = self._merge_sort(izquierda)
            derecha = self._merge_sort(derecha)

            return self._merge(izquierda, derecha)
        return datos

    def _merge(self, izquierda, derecha):
        resultado = []
        i = j = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        return resultado

    def dijkstra(self, inicio, fin):
        visitados = {inicio: 0}
        camino = {}

        nodos = set(self.datos.keys())

        while nodos:
            min_nodo = None
            for nodo in nodos:
                if nodo in visitados:
                    if min_nodo is None:
                        min_nodo = nodo
                    elif visitados[nodo] < visitados[min_nodo]:
                        min_nodo = nodo

            if min_nodo is None:
                break

            nodos.remove(min_nodo)
            peso_actual = visitados[min_nodo]

            for vecino, peso in self.datos[min_nodo].items():
                peso_total = peso_actual + peso
                if vecino not in visitados or peso_total < visitados[vecino]:
                    visitados[vecino] = peso_total
                    camino[vecino] = min_nodo

        return visitados, camino
    def comprobar(self, inicio, fin):
        if inicio not in self.datos or fin not in self.datos:
            print("Error: Uno de los nodos especificados no existe en el grafo.")
            return False


    def floyd_warshall(self):
        distancias = {nodo: {vecino: float('inf') for vecino in self.datos} for nodo in self.datos}
        for nodo in self.datos:
            distancias[nodo][nodo] = 0
            for vecino, peso in self.datos[nodo].items():
                distancias[nodo][vecino] = peso

        for k in self.datos:
            for i in self.datos:
                for j in self.datos:
                    if distancias[i][k] + distancias[k][j] < distancias[i][j]:
                        distancias[i][j] = distancias[i][k] + distancias[k][j]

        return distancias

class ProgramaPrincipal:
    def __init__(self):
        self.algoritmo = None
        self.lista = None
        self.grafo = Algoritmo({
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        })

    def main(self):
        while True:
            self.algoritmo = Algoritmo()
            print()
            print("Menú:")
            print("1. Ingresar lista de enteros")
            print("2. Buscar elemento por búsqueda lineal")
            print("3. Buscar elemento por búsqueda binaria")
            print("4. Buscar elemento por divide y venceras")
            print("5. Buscar elemento por búsqueda voraz")
            print("6. Ordenar lista con heap sort")
            print("7. Ordenar lista con merge sort")
            print("8. Aplicar algoritmo de Dijkstra")
            print("9. Aplicar algoritmo de Floyd-Warshall")
            print("10. Salir")


            opcion = input("Elige una opción (1-10): ")
            print()

            if opcion == "1":
                datos_usuario = input("Introduce la lista de enteros separados por espacio: ")
                try:
                    datos_usuario = list(map(int, datos_usuario.split()))
                    self.lista = Algoritmo(datos_usuario)
                    print("Lista ingresada:", self.lista.datos)
                except ValueError:
                    print("Error: Debes ingresar una lista de enteros separados por espacio.")
                    print("Por ejemplo: 1 2 3 4 5")


            elif opcion == "2":
                if self.lista:
                    elemento = int(input("Introduce el elemento a buscar  por búsqueda lineal: "))
                    resultado = self.lista.busqueda_lineal(elemento)
                    if resultado != -1:
                        print(f"Elemento encontrado en la posición {resultado}.")
                    else:
                        print("Elemento no encontrado.")
                else:
                    print("Debes ingresar una lista de enteros primero.")

            elif opcion == "3":
                if self.lista:
                    elemento = int(input("Introduce el elemento a buscar por búsqueda binaria: "))
                    resultado = self.lista.busqueda_binaria(elemento)
                    if resultado != -1:
                        print(f"Elemento encontrado en la posición {resultado}.")
                    else:
                        print("Elemento no encontrado.")
                else:
                    print("Debes ingresar una lista de enteros primero.")

            elif opcion == "4":
                if self.lista:
                    elemento = int(input("Introduce el elemento a buscar divide y venceras: "))
                    resultado = self.lista.divide_y_venceras(elemento)
                    if resultado != -1:
                        print(f"Elemento encontrado en la posición {resultado}.")
                    else:
                        print("Elemento no encontrado.")
                else:
                    print("Debes ingresar una lista de enteros primero.")


            elif opcion == "5":

                if self.lista:

                    elemento = int(input("Introduce el elemento a buscar búsqueda voraz: "))

                    resultado = self.lista.busqueda_voraz(elemento)

                    if resultado != -1:

                        print(f"Elemento encontrado en la posición {resultado}.")

                    else:

                        print("Elemento no encontrado.")

                else:

                    print("Debes ingresar una lista de enteros primero.")

            elif opcion == "6":
                if self.lista:
                    print("Lista ordenada con heap sort:", self.lista.heap_sort())
                else:
                    print("Debes ingresar una lista de enteros primero.")

            elif opcion == "7":
                if self.lista:
                    print("Lista ordenada con merge sort:", self.lista.merge_sort())
                else:
                    print("Debes ingresar una lista de enteros primero.")

            elif opcion == "8":
                if self.grafo:
                    inicio = input("Introduce el nodo inicial: ")
                    fin = input("Introduce el nodo final: ")
                    if self.grafo.comprobar(inicio,fin) != False:
                        visitados, camino = self.grafo.dijkstra(inicio, fin)

                        print("Distancias desde el nodo inicial hasta los demás nodos:")
                        for nodo, distancia in visitados.items():
                            print(f"{nodo}: {distancia}")

                        print("\nCamino desde el nodo inicial hasta el nodo final:")
                        actual = fin
                        camino_actual = []
                        while actual != inicio:
                            camino_actual.append(actual)
                            actual = camino.get(actual, None)
                        camino_actual.append(inicio)
                        camino_actual.reverse()
                        print(" -> ".join(camino_actual))
                else:
                    print("Debes ingresar un grafo primero.")

            elif opcion == "9":
                if self.grafo:
                    distancias = self.grafo.floyd_warshall()
                    print("Matriz de distancias más cortas entre todos los pares de nodos:")
                    for nodo, vecinos in distancias.items():
                        print(f"{nodo}: {vecinos}")
                else:
                    print("Debes ingresar un grafo primero.")


            elif opcion == "10":
                print("¡Gracias por usar!")
                break

            else:
                print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    programa = ProgramaPrincipal()
    programa.main()