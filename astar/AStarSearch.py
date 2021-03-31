# Definição de um nó em cada grafo
class Nodo:

    # Construtor principal
    def __init__(self, name: str, pai: str):
        self.nome = name
        self.pai = pai
        self.g = 0          # Distância para o nó inicial
        self.h = 0          # Distância para o objetivo
        self.f = 0          # Custo total

    # Sobrescrevendo o método que testa se dois objetos são iguais.
    # Serão se eles possuírem o mesmo nome
    def __eq__(self, other):
        return self.nome == other.nome

    # Ordenar os nós. O método os colocará por ordem de custo total (crescente)
    def __lt__(self, other):
        return self.f < other.f

    # Imprime informações sobre o nó no console
    def __repr__(self):
        return ('({0},{1})'.format(self.nome, self.f))


# Representação de um grafo convencional, direcionado ou não direcionado
class Grafo:

    # Construtor principal
    def __init__(self, grafo_dic=None, direcionado=True):
        self.grafo_dic = grafo_dic or {}
        self.direcionado = direcionado
        if not direcionado:
            self.tornar_não_direcionado()

    # Criar um grafo não-direcionado, adicionando nós paralelos simétricos
    # ao nó principal
    def tornar_não_direcionado(self):
        for a in list(self.grafo_dic.keys()):
            for (b, dist) in self.grafo_dic[a].items():
                self.grafo_dic.setdefault(b, {})[a] = dist

    # Adiciona uma ligação de A para B de uma certa distância, e também
    # adiciona uma ligação inversa se o grafo for não direcionado
    def conectar(self, A, B, distancia=1):
        self.grafo_dic.setdefault(A, {})[B] = distancia
        if not self.direcionado:
            self.grafo_dic.setdefault(B, {})[A] = distancia

    # Obter os vizinhos ou um vizinho
    def obter(self, a, b=None):
        links = self.grafo_dic.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # Retorna uma lista de nós presentes no grafo
    def nodos(self):
        s1 = set([k for k in self.grafo_dic.keys()])
        s2 = set([k2 for v in self.grafo_dic.values() for k2, v2 in v.items()])
        nodos = s1.union(s2)
        return list(nodos)


# Busca A* (A-Estrela). Utiliza busca em largura, somada a uma heurística baseada
# na distância ao objetivo final
def busca_aestrela(grafo, heuristicas, inicio, final):

    # Lista de nós abertos e fechados, que são utilizados para controle de
    # visitação sobre o grafo
    abertos = []
    fechados = []

    # Estabelecer um nó inicial e final para o grafo. Obviamente o início aponta para o
    # ponto de partida para a busca, e o nó final o objetivo
    no_inicial = Nodo(inicio, None)
    no_objetivo = Nodo(final, None)

    # Adiciona o nó inicial na lista de nós abertos. Esta lista controla os nós ainda
    # não visitados
    abertos.append(no_inicial)

    # Iteragir sobre a lista de nós abertos, até que todos tenham sido visitados pelo
    # menos uma vez
    while len(abertos) > 0:

        # Ordenar a lista de nós abertos para sempre visitar o próximo nó mais próximo
        # do objetivo final. Lembrando que a ordenação dos grafos ocorre pelo custo total
        # até o objetivo !!
        abertos.sort()

        # Uma vez ordenada a lista, no início dela teremos o nó de menor custo. Pegamos ele
        # e faremos a próxima visita sobre ele
        no_corrente = abertos.pop(0)

        # Adiciona o nó corrente na lista de nós fechados ou visitados
        fechados.append(no_corrente)

        # Se o nó corrente é o objetivo, então a busca localizou o nó e o seu caminho
        # mais próximo. No loop abaixo é feito o caminho do nó corrente (e objetivo final)
        # até o seu pai
        if no_corrente == no_objetivo:
            caminho = []
            while no_corrente != no_inicial:
                caminho.append(no_corrente.nome + ': ' + str(no_corrente.g))
                no_corrente = no_corrente.pai
            caminho.append(no_inicial.nome + ': ' + str(no_inicial.g))
            # Retorna o caminho na ordem inversa ... pois, no loop acima, é feito um caminho
            # do objetivo ao início. Mas, queremos o caminho do início ao objetivo, :)
            return caminho[::-1]

        # Se chegou até aqui, é pq não atingimos o objetivo final !

        # Vamos obter os vizinhos do nó corrente, e fazer uma visitação em cada um, sempre
        # respeitando a heurística da distância total ao objetivo
        vizinhos = grafo.obter(no_corrente.nome)

        # Iteragir sobre todos os vizinhos do nó atual
        for chave, valor in vizinhos.items():

            # Criar um nó vizinho, a partir da chave correntamente selecionado
            vizinho = Nodo(chave, no_corrente)

            # Se o vizinho selecionado já foi visitado, ele não é mais considerado !
            if (vizinho in fechados):
                continue

            # Calcular o custo total do caminho. Na tabela de heurísticas temos a distância
            # total em linha reta do nó atual para o objetivo
            vizinho.g = no_corrente.g + grafo.obter(no_corrente.nome, vizinho.nome)
            vizinho.h = heuristicas.get(vizinho.nome)
            vizinho.f = vizinho.g + vizinho.h

            # Verificar se o vizinho possui custo menor que o atual, e não está na lista
            # de nós abertos
            if (adicionar_aberto(abertos, vizinho) == True):

                # Everything is green, add neighbor to open list
                abertos.append(vizinho)

    # Retorna vazio. Ou seja, nenhum caminho encontrado
    return None


# Adiciona se o vizinho deve ser visitado ou não. Note que o IF testa se o caminho deste
# vizinho possui distância total maior que o nó atual, este método retorna Falso ...
def adicionar_aberto(abertos, vizinho):
    for node in abertos:
        if (vizinho == node and vizinho.f > node.f):
            return False
    return True


#########################################################################################

def main():
    # Criar o grafo
    grafo = Grafo()

    # Criar as cidades, suas conexões e suas distâncias

    grafo.conectar('Curitiba', 'Joinville', 120)
    grafo.conectar('Joinville', 'Itajaí', 93)
    grafo.conectar('Itajaí', 'Florianópolis', 101)
    grafo.conectar('Florianópolis', 'Criciúma', 207)
    grafo.conectar('Criciúma', 'Torres', 104)
    grafo.conectar('Torres', 'Osório', 95)
    grafo.conectar('Osório', 'Porto Alegre', 104)

    grafo.conectar('Curitiba', 'Mafra', 116)
    grafo.conectar('Mafra', 'Papanduva', 53)
    grafo.conectar('Papanduva', 'Santa Cecília', 90)
    grafo.conectar('Santa Cecília', 'Ponte Alta', 68)
    grafo.conectar('Ponte Alta', 'Lages', 42)
    grafo.conectar('Lages', 'Vacaria', 108)
    grafo.conectar('Vacaria', 'Caxias do Sul', 112)
    grafo.conectar('Caxias do Sul', 'Novo Hamburgo', 97)
    grafo.conectar('Novo Hamburgo', 'Porto Alegre', 50)

    # O grafo em questão é não direcionado !

    grafo.tornar_não_direcionado()

    # Criação da heurística. Neste caso, a heurística é a distância em linha reta para
    # o objetivo final
    heuristicas = {}
    heuristicas['Joinville'] = 622
    heuristicas['Itajaí'] = 536
    heuristicas['Florianópolis'] = 462
    heuristicas['Criciúma'] = 285
    heuristicas['Torres'] = 193
    heuristicas['Osório'] = 104
    heuristicas['Mafra'] = 586
    heuristicas['Papanduva'] = 538
    heuristicas['Santa Cecília'] = 449
    heuristicas['Ponte Alta'] = 380
    heuristicas['Lages'] = 343
    heuristicas['Vacaria'] = 239
    heuristicas['Caxias do Sul'] = 127
    heuristicas['Novo Hamburgo'] = 49
    heuristicas['Porto Alegre'] = 0

    # Executar a busca A*

    path = busca_aestrela(grafo, heuristicas, 'Curitiba', 'Porto Alegre')
    print(path)
    print()


# Rodar o método Main, :)
if __name__ == "__main__": main()