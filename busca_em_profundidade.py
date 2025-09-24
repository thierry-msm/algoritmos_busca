def busca_em_profundidade(grafo, inicio, objetivo):
    """
    Implementa o algoritmo de Busca em Profundidade (DFS) para encontrar um caminho
    entre um nó inicial e um nó objetivo em um grafo.

    Args:
        grafo (dict): Um dicionário que representa o grafo, onde as chaves são os nós
                      e os valores são listas de nós adjacentes.
        inicio (str): O nó de partida da busca.
        objetivo (str): O nó que se deseja alcançar.

    Returns:
        list or None: Uma lista de nós representando o caminho do início ao objetivo,
                      ou None se nenhum caminho for encontrado.
    """
    # Usamos uma pilha para armazenar os nós a serem visitados.
    # Cada item da pilha será uma tupla (nó_atual, caminho_ate_aqui).
    # O caminho_ate_aqui é uma lista de nós que levam ao nó_atual.
    pilha = [(inicio, [inicio])]

    # Um conjunto para armazenar os nós já visitados, evitando ciclos e reprocessamento.
    visitados = set()

    print(f"Iniciando Busca em Profundidade de '{inicio}' para '{objetivo}'...")

    while pilha:
        # Desempilha o nó atual e o caminho até ele.
        # A DFS explora o nó mais recentemente adicionado (topo da pilha).
        no_atual, caminho = pilha.pop()
        # no_atual = 'K'
        # caminho = ['A', 'C', 'G', 'K']
        print(f"  Explorando sala: {no_atual} (Caminho atual: {' -> '.join(caminho)})")

        # Se o nó atual já foi visitado, pulamos para o próximo.
        # Isso é importante para evitar loops infinitos em grafos com ciclos.
        if no_atual in visitados:
            continue

        # Marca o nó atual como visitado.
        visitados.add(no_atual)

        # Se o nó atual é o objetivo, encontramos um caminho!
        if no_atual == objetivo:
            print(f"\nCaminho encontrado! De '{inicio}' para '{objetivo}':")
            return caminho

        # Explora os vizinhos do nó atual.
        # Adicionamos os vizinhos em ordem inversa para que, ao desempilhar,
        # eles sejam processados em uma ordem "natural" (se a lista de adjacência for ordenada).
        # Ou simplesmente adicionamos e deixamos a pilha fazer seu trabalho.
        for vizinho in reversed(grafo.get(no_atual, [])): # Usamos reversed para manter a ordem de exploração mais intuitiva
            if vizinho not in visitados:
                novo_caminho = caminho + [vizinho]
                pilha.append((vizinho, novo_caminho)) #adiciona tupla desse nó e caminho dele
                print(f"    Adicionando vizinho '{vizinho}' à pilha. Novo caminho potencial: {' -> '.join(novo_caminho)}")

    # Se a pilha ficar vazia e o objetivo não foi encontrado, significa que não há caminho.
    print(f"\nNenhum caminho encontrado de '{inicio}' para '{objetivo}'.")
    return None

# --- Exemplo de Uso com o Labirinto ---

# Definindo o labirinto
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
    'K': ['G', 'N', 'H'],
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

#entradas
inicio = input("Sala inicial: ").strip().upper()
fim = input("Sala final: ").strip().upper()

caminho_dfs_1 = busca_em_profundidade(labirinto, inicio, fim)

print(f"--- Buscando caminho de {inicio} para {fim} ---")
if caminho_dfs_1:
    print(f"Caminho encontrado de {inicio} para {fim}: {' -> '.join(caminho_dfs_1)}")
    print(f"O caminho tem {len(caminho_dfs_1) - 1} passos.")
else:
    print(f"Não foi possível encontrar um caminho de {inicio} para {fim}.")
