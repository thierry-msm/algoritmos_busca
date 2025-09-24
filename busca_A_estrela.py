import heapq

#Busca A*

# Definição do labirinto (grafo)
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

# Coordenadas das salas para cálculo da heurística
coordenadas_salas = {
    'A': [(0, 0), (0, 1)],
    'B': [(1, 0), (2, 0)],
    'C': [(1, 1), (2, 1)],
    'D': [(3, 0), (3, 1)],
    'E': [(4, 0), (5, 0), (4, 1), (5, 1)],
    'F': [(6, 0), (6, 1)],
    'G': [(0, 2), (1, 2)],
    'H': [(2, 2), (2, 3)],
    'I': [(3, 2), (4, 2)],
    'J': [(5, 2), (6, 2)],
    'K': [(0, 3), (1, 3)],
    'L': [(3, 3), (3, 4), (4, 3), (4, 4)],
    'M': [(5, 3), (5, 4), (6, 3), (6, 4)],
    'N': [(0, 4), (0, 5), (1, 4), (1, 5)],
    'O': [(2, 4), (2, 5)],
    'P': [(3, 5), (4, 5), (5, 5), (6, 5)],
    'Q': [(0, 6), (0, 7), (1, 6), (1, 7)],
    'R': [(2, 6), (2, 7)],
    'S': [(3, 6), (3, 7)],
    'T': [(4, 6), (4, 7), (5, 6), (5, 7)],
    'U': [(6, 6), (6, 7)]
}

# Custos das salas
#Salas 2*1 ou 1*2 custo = 1 Salas 2*2 ou 1*4 = 2
custo_salas = {
    'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 2, 'F': 1,
    'G': 1, 'H': 1, 'I': 1, 'J': 1, 'K': 1, 'L': 2,
    'M': 2, 'N': 2, 'O': 2, 'P': 2, 'Q': 2, 'R': 1,
    'S': 1, 'T': 2, 'U': 1
}

# Função auxiliar para obter a coordenada representativa de uma sala
def get_representative_coord(room):
    if room in coordenadas_salas and coordenadas_salas[room]:
        return coordenadas_salas[room][0]
    raise ValueError(f"Sala '{room}' não possui coordenadas definidas.")

# Função da heurística: Distância de Manhattan
def manhattan_distance(room1, room2):
    coord1 = get_representative_coord(room1)
    coord2 = get_representative_coord(room2)
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

# Implementação do Algoritmo de Busca A* com custo das salas
def a_star_search(graph, start, goal):
    # open_set é uma fila de prioridade que armazena tuplas (f_score, nó)
    open_set = []
    heapq.heappush(open_set, (0, start)) # f_score inicial para o nó de partida é apenas h(start)

    # came_from[n] armazena o nó que precede n no caminho mais barato conhecido até agora.
    came_from = {}

    # g_score[n] é o custo do caminho mais barato do início até n.
    g_score = {node: float('inf') for node in graph} #inf - inicialmente o custo é infinito exceto o inicial
    g_score[start] = 0

    # f_score[n] = g_score[n] + h(n). É a estimativa do custo total do caminho mais barato do início ao objetivo, passando por n.
    f_score = {node: float('inf') for node in graph}
    f_score[start] = manhattan_distance(start, goal)

    #print(f"Iniciando busca A* de '{start}' para '{goal}'...")

    while open_set: # Explora todos os nós na fila de prioridade para descobrir o melhor caminho
        # Extrai o nó com o menor f_score da fila de prioridade
        current_f_score, current_node = heapq.heappop(open_set)

        #print(f"Expandindo nó '{current_node}' (f_score: {current_f_score}, g_score: {g_score[current_node]}, h_score: {manhattan_distance(current_node, goal)})")

        # Se o nó atual é o objetivo, reconstruímos o caminho e o retornamos.
        if current_node == goal:
            path = []
            temp_node = goal
            while temp_node in came_from:
                path.append(temp_node)
                temp_node = came_from[temp_node]
            path.append(start) # Adiciona o nó inicial ao caminho
            #print(f"Caminho encontrado: {path[::-1]}")
            return path[::-1] # Inverte o caminho para ir do início ao objetivo

        # Explora os vizinhos do nó atual
        for neighbor in graph[current_node]:
            # O custo de ir do nó atual para um vizinho é o custo da sala vizinha.
            tentative_g_score = g_score[current_node] + custo_salas[neighbor]

            # Se encontramos um caminho mais curto para o vizinho
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node # Atualiza o predecessor
                g_score[neighbor] = tentative_g_score # Atualiza o g_score
                f_score[neighbor] = g_score[neighbor] + manhattan_distance(neighbor, goal) # Atualiza o f_score
                heapq.heappush(open_set, (f_score[neighbor], neighbor)) # Adiciona o vizinho à fila de prioridade

    print(f"Não foi possível encontrar um caminho de '{start}' para '{goal}'.")
    return None # Nenhum caminho encontrado
  
#Teste 1:
start_room = 'A'
end_room = 'U'

path_a_star = a_star_search(labirinto, start_room, end_room)

if path_a_star:
    print(f"\n--- Resultado da Busca A* ---")
    print(f"Caminho de '{start_room}' para '{end_room}': {' -> '.join(path_a_star)}")
    print(f"Número de passos: {len(path_a_star) - 1}")
    print(f"Custo total do caminho: {sum(custo_salas[room] for room in path_a_star[1:])}")
else:
    print(f"\nNão foi possível encontrar um caminho de '{start_room}' para '{end_room}'.")

# Teste 1: B -> P
start_room_1 = 'B'
end_room_1 = 'P'

path_a_star_1 = a_star_search(labirinto, start_room_1, end_room_1)

if path_a_star_1:
    print(f"\n--- Resultado da Busca A* (Teste 1: B -> P) ---")
    print(f"Caminho de '{start_room_1}' para '{end_room_1}': {' -> '.join(path_a_star_1)}")
    print(f"Número de passos: {len(path_a_star_1) - 1}")
    print(f"Custo total do caminho: {sum(custo_salas[room] for room in path_a_star_1[1:])}")
else:
    print(f"\nNão foi possível encontrar um caminho de '{start_room_1}' para '{end_room_1}'.")

# Teste 2: H -> H
start_room_2 = 'H'
end_room_2 = 'H'

path_a_star_2 = a_star_search(labirinto, start_room_2, end_room_2)

if path_a_star_2:
    print(f"\n--- Resultado da Busca A* (Teste 2: H -> H) ---")
    print(f"Caminho de '{start_room_2}' para '{end_room_2}': {' -> '.join(path_a_star_2)}")
    print(f"Número de passos: {len(path_a_star_2) - 1}")
    print(f"Custo total do caminho: {sum(custo_salas[room] for room in path_a_star_2[1:])}")
else:
    print(f"\nNão foi possível encontrar um caminho de '{start_room_2}' para '{end_room_2}'.")

# Teste 3: C -> M
start_room_3 = 'C'
end_room_3 = 'M'

path_a_star_3 = a_star_search(labirinto, start_room_3, end_room_3)

if path_a_star_3:
    print(f"\n--- Resultado da Busca A* (Teste 3: C -> M) ---")
    print(f"Caminho de '{start_room_3}' para '{end_room_3}': {' -> '.join(path_a_star_3)}")
    print(f"Número de passos: {len(path_a_star_3) - 1}")
    print(f"Custo total do caminho: {sum(custo_salas[room] for room in path_a_star_3[1:])}")
else:
    print(f"\nNão foi possível encontrar um caminho de '{start_room_3}' para '{end_room_3}'.")