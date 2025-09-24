import collections

def busca_em_largura(grafo, inicio, fim):
    """
    Algoritmo de Busca em Largura (BFS) para encontrar o caminho mais curto
    entre dois nós em um grafo.

    Args:
        grafo (dict): Um dicionário representando as salas que se conectam no grafo. (ou nós que se conectam)
        inicio (str): O nó de partida.
        fim (str): O nó de destino.

    Returns:
        list: Uma lista de nós representando o caminho do início ao fim.
              Retorna uma lista vazia se não houver caminho.
    """
    fila = collections.deque([[inicio]])
    visitados = {inicio}

    if inicio == fim:
        return [inicio]

    while fila:
        caminho = fila.popleft()
        no_atual = caminho[-1]

        if no_atual == fim:
            return caminho

        for vizinho in grafo.get(no_atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)

    return []

# --- Programa Principal ---

# 1. Representação CORRETA do labirinto como um grafo
labirinto = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['A', 'B', 'G'],
    'D': ['B', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'J'],
    'G': ['C', 'K', 'H'],
    'H': ['K', 'G', 'L', 'I'],
    'I': ['H', 'J'],
    'J': ['F', 'I', 'M'],
    'K': ['G', 'N', 'H' ],
    'L': ['H', 'M'],
    'M': ['J', 'L', 'P'],
    'N': ['K', 'O', 'Q'],
    'O': ['N', 'P'],
    'P': ['M', 'O', 'T'],
    'Q': ['N', 'R'],
    'R': ['Q', 'S'],
    'S': ['R', 'T'],
    'T': ['P', 'S', 'U'],
    'U': ['T']
}

# 2. Entradas
sala_inicial = input("Sala inicial: ").strip().upper()
sala_final = input("Sala final: ").strip().upper()
# 3. Executando o algoritmo com o grafo corrigido
caminho_encontrado = busca_em_largura(labirinto, sala_inicial, sala_final)

# 4. Exibindo o resultado
if caminho_encontrado:
    print(f"✅ Caminho encontrado de '{sala_inicial}' para '{sala_final}':")
    print(" -> ".join(caminho_encontrado))
    print(f"O caminho mais curto tem {len(caminho_encontrado) - 1} passos.")
else:
    print(f"❌ Não foi possível encontrar um caminho de '{sala_inicial}' para '{sala_final}'.")