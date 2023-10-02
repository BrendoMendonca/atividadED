from grafo import Grafo

def load_from(fileName): 
    f = open(fileName, 'r')
    n = int(f.readline()) #n recebe a primeira linha do arquivo lido que contem a quantidade de vértices

    g = Grafo(n) #instancia da classe Grafo com parâmetro n

    l = 0 #l representa a linha da matriz
    for line in f:
        line.strip() #remove espaços em branco em excesso
        numeros = line.split("\t") #numeros recebe os elementos da linha separados com \t
        c = 0 #representa a coluna da matriz
        for i in numeros:
            if(c == g.num_vertices): #verifica se chegou ao final da linha
                break
            g.matriz[l][c] = int(i) #preenche a matriz com os elementos do arquivo
            if(g.matriz[l][c] > 0):
                g.list[l].append(c) #se o valor for maior que 0, o vértice é adicionado à lista de adjacentes
            
            c += 1 #incremento da coluna
        l += 1 #incremento da linha
    return g

def print_matriz(matriz): #função para imprimir a matriz
    for row in matriz:
        print(row)


gr = load_from("pcv4.txt")
#gr.print()
print("Matriz de Adjacência:")
print_matriz(gr.matriz)
dist, ant = gr.bfs(3)
print(dist)
print(ant)