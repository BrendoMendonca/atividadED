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

        while Q.empty() != True: #verifica se a lista Q não está vazia
            p = Q.get() #remove o elemento da lista e o armazena na variável p
            print("Vertice: " + str(p)) #exibe o elemento removido
        
            for v in self.list[p]: #loop para iterar com os elementos da lista de adjacencia do vertice p
                if isVisited[v] == False: #verifica se o vertice adjacente não foi visitado
                    dist[v] = dist[p] + 1 #calcula a distancia do vertice adjacente ao vertice de origem
                    ant[v] = p #atribui o valor de p ao antecessor de v na lista de antecessores
                    Q.put(v) #adiciona v à fila
                    isVisited[v] = True #v é marcado como visitado
        
        return dist, ant