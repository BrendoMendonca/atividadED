import queue #biblioteca para trabalhar com filas

class Grafo:
    def __init__(self, n): #construtor python
        self.num_vertices = n
        self.matriz = [[0 for _ in range(n)] for _ in range(n)] #inicialização da matriz nxn zerada
        self.list = [[]for _ in range(n)] #inicialização da lista de tamanho n vazia

    def print(self):
        #print(self.matriz)
        print(self.list)
    
    def bfs(self, source):
        dist = [-1 for _ in range(self.num_vertices)] #cria uma lista com valores -1
        ant = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)] #cria uma lista booleana onde todos os valores sao False
        Q = queue.Queue() #criação do objeto do tipo Queue(fila)
        Q.put(source)#adiciona elemento(vertice) na fila
        isVisited[source] = True #informa à lista que o vertice foi visitado
        dist[source] = 0

        print("Ordem de vértices visitados")
        while Q.empty() != True: #verifica se a fila Q não está vazia
            p = Q.get() #remove o elemento da fila e o armazena na variável p
            print("Vertice: " + str(p)) #exibe o elemento removido
        
            for v in self.list[p]: #loop para iterar com os elementos da lista de adjacencia do vertice p
                if isVisited[v] == False: #verifica se o vertice adjacente não foi visitado
                    dist[v] = dist[p] + 1 #calcula a distancia do vertice adjacente ao vertice de origem
                    ant[v] = p #atribui o valor de p ao antecessor de v na lista de antecessores
                    Q.put(v) #adiciona v à fila
                    isVisited[v] = True #v é marcado como visitado
        
        return dist, ant
    
    def bfs_caminho(self, s, t, n_aresta):
        #inicializações de listas e fila
        dist = [-1 for _ in range(self.num_vertices)] #cria uma lista com valores -1
        ant = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)] #cria uma lista booleana onde todos os valores sao False
        Q = queue.Queue() #criação do objeto do tipo Queue(fila)
        Q.put(s)#adiciona elemento(vertice) na fila
        isVisited[s] = True #informa à lista que o vertice foi visitado
        dist[s] = 0

        caminho = [[] for _ in range(self.num_vertices)]
        caminho[s] = [s] #registra o caminho percorrido durante a BFS

        while not Q.empty():
            p = Q.get()

            for v in self.list[p]:
                if not isVisited[v]:
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    Q.put(v)
                    isVisited[v] = True

                    #atualiza o caminho até o destino
                    caminho[v] = caminho[p] + [v]
                    #verifica se o vértice é o de destino e se a distancia é igual a quantiade de arestas
                    if v == t and dist[v] == n_aresta: 
                        return caminho[v]
        
        return "Não há caminho entre os vértices"