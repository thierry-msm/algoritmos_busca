import heapq
# Busca gulosa (Greedy Search)
# Definindo o labirinto (fornecido por você)
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

# Coordenadas das salas (Imaginando que ele fosse uma matriz 7*8)
coordenadas_salas = {
    'A': [(0, 0), (0, 1)],
    'B': [(1, 0), (2,0)],
    'C': [(1, 1), (2, 1)],
    'D': [(3, 0), (3,1)],
    'E': [(4, 0),  (5, 0), (4, 1), (5, 1)],
    'F': [(6, 0), (6, 1)],
    'G': [(0, 2), (1, 2)],
    'H': [(2, 2), (2, 3)],
    'I': [(3, 2), (4, 2)],
    'J': [(5, 2), (6,2)],
    'K': [(0, 3), (1, 3)],
    'L': [(3, 3), (3, 4), (4, 3), (4, 4)],
    'M': [(5, 3), (5, 4), (6, 3), (6, 4)],
    'N': [(0, 4), (0, 5), (1,4), (1,5)],
    'O': [(2, 4), (2, 5)],
    'P': [(3, 5), (4, 5), (5,5), (6,5)],
    'Q': [(0, 6), (0,7), (1,6), (1,7)],
    'R': [(2, 6), (2,7)],
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

# Extraindo uma única coordenada representativa para cada sala para o cálculo da heurística.
# Usamos a primeira coordenada fornecida para cada sala.
room_single_coords = {room: coords[0] for room, coords in coordenadas_salas.items()}

def manhattan_distance(room1, room2, room_coords_map):
    """
    Calcula a Distância de Manhattan entre duas salas.
    Args:
        room1 (str): Nome da primeira sala.
        room2 (str): Nome da segunda sala (geralmente a sala objetivo).
        room_coords_map (dict): Dicionário mapeando nomes de salas para suas coordenadas (x, y), Ex A:(0,0).
    Returns:
        int: A distância de Manhattan entre as duas salas.
    """
    x1, y1 = room_coords_map[room1]
    x2, y2 = room_coords_map[room2]
    return abs(x1 - x2) + abs(y1 - y2) #abs pega módulo

def greedy_search(graph, start, goal, room_coords_map, room_costs):
    """
    Implementa o algoritmo de Busca Gulosa considerando o custo do tamanho das salas.

    Args:
        graph (dict): O grafo do labirinto onde as chaves são salas e os valores são listas de salas vizinhas.
        start (str): A sala inicial.
        goal (str): A sala objetivo.
        room_coords_map (dict): Dicionário com as coordenadas (x, y) de cada sala para cálculo da heurística.
        room_costs (dict): Dicionário com os custos associados a cada sala.

    Returns:
        list: A sequência de salas do caminho encontrado do início ao objetivo, ou None se nenhum caminho for encontrado.
    """

    # Confere se as salas estão no labirinto
    if start not in graph or goal not in graph:
        print(f"Erro: Sala inicial '{start}' ou sala objetivo '{goal}' não encontrada(s) no labirinto.")
        return None

    # A fila de prioridade armazena tuplas: (custo_total, sala_atual, caminho_ate_a_sala_atual)
    # O custo_total é a soma do custo heurístico (distância de Manhattan) e o custo da sala.
    priority_queue = []
    # O primeiro item na fila é a sala inicial, com seu custo total e o caminho até ela.
    heapq.heappush(priority_queue, (manhattan_distance(start, goal, room_coords_map) + room_costs[start], start, [start]))

    # Conjunto para manter o controle das salas já visitadas para evitar ciclos e reprocessamento.
    visited = set()

    while priority_queue:
        # Pega a sala com o menor custo total da fila de prioridade
        total_cost, current_room, path = heapq.heappop(priority_queue)

        # Se a sala atual é a sala objetivo, encontramos o caminho
        if current_room == goal:
            return path

        # Se já visitamos esta sala, pulamos para a próxima iteração
        if current_room in visited:
            continue

        # Marcamos a sala atual como visitada
        visited.add(current_room)

        # Exploramos os vizinhos da sala atual
        for neighbor in graph.get(current_room, []):
            # Se o vizinho ainda não foi visitado
            if neighbor not in visited:
                # Criamos um novo caminho adicionando o vizinho
                new_path = path + [neighbor]
                # Calculamos o custo heurístico do vizinho até o objetivo
                neighbor_h_cost = manhattan_distance(neighbor, goal, room_coords_map)
                # Adicionamos o custo da sala vizinha
                neighbor_total_cost = neighbor_h_cost + room_costs[neighbor]
                # Adicionamos o vizinho à fila de prioridade
                heapq.heappush(priority_queue, (neighbor_total_cost, neighbor, new_path))

    # Se a fila de prioridade ficar vazia e não encontrarmos o objetivo, significa que não há caminho
    return None

# --- Exemplo de Uso ---
print("--- Testando o Algoritmo de Busca Gulosa ---")

# Cenário 1: Caminho simples
start_room_1 = 'A'
goal_room_1 = 'U'
print(f"\nBuscando caminho de {start_room_1} para {goal_room_1} (Busca Gulosa):")
path_1 = greedy_search(labirinto, start_room_1, goal_room_1, room_single_coords, custo_salas)
if path_1:
    print(f"Caminho encontrado: {' -> '.join(path_1)}")
else:
    print("Nenhum caminho encontrado.")

# Cenário 2: Outro caminho
start_room_2 = 'B'
goal_room_2 = 'P'
print(f"\nBuscando caminho de {start_room_2} para {goal_room_2} (Busca Gulosa):")
path_2 = greedy_search(labirinto, start_room_2, goal_room_2, room_single_coords, custo_salas)
if path_2:
    print(f"Caminho encontrado: {' -> '.join(path_2)}")
else:
    print("Nenhum caminho encontrado.")

# Cenário 3: Sala inicial e final iguais
start_room_3 = 'H'
goal_room_3 = 'H'
print(f"\nBuscando caminho de {start_room_3} para {goal_room_3} (Busca Gulosa):")
path_3 = greedy_search(labirinto, start_room_3, goal_room_3, room_single_coords, custo_salas)
if path_3:
    print(f"Caminho encontrado: {' -> '.join(path_3)}")
else:
    print("Nenhum caminho encontrado.")

# Cenário 4: Caminho que pode ilustrar a natureza "gulosa"
start_room_4 = 'C'
goal_room_4 = 'M'
print(f"\nBuscando caminho de {start_room_4} para {goal_room_4} (Busca Gulosa):")
path_4 = greedy_search(labirinto, start_room_4, goal_room_4, room_single_coords, custo_salas)
if path_4:
    print(f"Caminho encontrado: {' -> '.join(path_4)}")
else:
    print("Nenhum caminho encontrado.")