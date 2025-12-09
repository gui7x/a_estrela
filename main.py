import heapq
import math

# implementacao com o grafo de exemplo -- caminho minimo entre os pontos A e E
grafo = {
    "A": [("B", 140), ("F", 150)],
    "B": [("A", 140), ("C", 120), ("D", 160)],
    "C": [("B", 120), ("D", 180)],
    "D": [("B", 160), ("C", 180), ("E", 110)],
    "E": [("D", 110), ("F", 170)],
    "F": [("A", 150), ("E", 170)],
}

# coordenadas ficticias
coords = {
    "A": (-8.0523, -34.9288),
    "B": (-8.0519, -34.9275),
    "C": (-8.0527, -34.9266),
    "D": (-8.0534, -34.9272),
    "E": (-8.0540, -34.9280),
    "F": (-8.0530, -34.9290),
}

def haversine(p1, p2):
    lat1, lon1 = p1
    lat2, lon2 = p2

    R = 6371000

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = phi2 - phi1
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2

    c = 2 * math.asin(math.sqrt(a))
    return R * c

def reconstruir_caminho(came_from, destino):
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = came_from[atual]
    caminho.reverse()
    return caminho

def a_estrela(grafo, coords, inicio, destino):
    fronteira = []
    heapq.heappush(fronteira, (0.0, inicio))

    g = {inicio: 0.0}
    came_from = {inicio: None}

    while fronteira:
        f_atual, atual = heapq.heappop(fronteira)

        if atual == destino:
            caminho = reconstruir_caminho(came_from, destino)
            return caminho, g[destino]

        for vizinho, peso in grafo.get(atual, []):
            novo_g = g[atual] + peso

            if vizinho not in g or novo_g < g[vizinho]:
                g[vizinho] = novo_g
                h = haversine(coords[vizinho], coords[destino])
                f = novo_g + h
                heapq.heappush(fronteira, (f, vizinho))
                came_from[vizinho] = atual

    return None, float("inf")

if __name__ == "__main__":
    caminho, custo = a_estrela(grafo, coords, "A", "E")
    print("Caminho encontrado:", caminho)
    print("Custo total (arestas):", custo)
