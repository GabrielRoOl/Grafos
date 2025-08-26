from contextlib import nullcontext

import networkx as nx
from matplotlib import pyplot as plt
from numpy.f2py.rules import aux_rules


class RedeSocial:
    def __init__(self):
        self.grafo = {}

    def adicionar_pessoa(self, nome):
        """
        Adiciona uma pessoa ao grafo, se ela ainda não existir.
        - grafo: o nosso array de amigos
        - nome: o nome da pessoa que vai ser adicionada
        """
        if nome not in self.grafo:
            self.grafo[nome] = []

        else:
            print(f"{nome} já existe na rede de amigos.")

    def adicionar_amizade(self, pessoa1, pessoa2):
        """
        Adiciona uma nova amizade entre duas pessoas
        Uma amizade é uma via de mão dupla, por isso adicionamos a conexão nos dois sentidos.
        """
        if pessoa1 in self.grafo and pessoa2 in self.grafo:
            if pessoa1 in self.grafo[pessoa2] or pessoa2 in self.grafo[pessoa1]:
                print(f"{pessoa1} e {pessoa2} já são amigos.")
                return
            if pessoa1 not in self.grafo[pessoa2]:
                self.grafo[pessoa2].append(pessoa1)

            if pessoa2 not in self.grafo[pessoa1]:
                self.grafo[pessoa1].append(pessoa2)
        else:
            print(f"{pessoa1} ou {pessoa2} não existem na lista de amigos.")
            exit()

    def sugerir_amigos(self, nome):
        """
        Mostra uma lista de amigos a partir dos amigos dessa pessoa
        """
        print(f'\nSugestão de amigos para {nome}: ')
        if nome not in self.grafo:
            print(f"{nome} não está cadastrado.")
            return None
        amigos = self.grafo[nome]

        resultado = []

        for amigo_direto in amigos:
            amigos_dos_amigos = self.grafo[amigo_direto].copy()
            if nome in amigos_dos_amigos:
                amigos_dos_amigos.remove(nome)

            resultado.extend(amigos_dos_amigos)

        return list(dict.fromkeys(resultado))

    def caminho(self, pessoa1, pessoa2):
        self.verificacao(pessoa1, pessoa2)

        plt.title("Grafo Amigos")

        G = nx.Graph(self.grafo)
        rota = nx.shortest_path(G, pessoa1, pessoa2)

        aresta_rota = []

        for i in range(len(rota) - 1):
            aresta = (rota[i], rota[i + 1])
            aresta_rota.append(aresta)

        return list(dict.fromkeys(aresta_rota))

    def visualizar_grafo(self):
        G = nx.Graph(self.grafo)
        # Calcula a posição dos nós uma única vez para que tudo fique alinhado
        pos = nx.spring_layout(G)

        # Camada 1: Vertices e as arestas de fundo
        nx.draw_networkx_nodes(G, pos, node_color='lightblue')

        # Camada 2: Nomes
        nx.draw_networkx_labels(G, pos)

        # Camada 3: Arestas do caminho por cima
        nx.draw_networkx_edges(G, pos, edge_color='gray', width=1)

        # Mostra tudo
        plt.show()

    def visualizar_caminho_entre(self, pessoa1, pessoa2):
        self.verificacao(pessoa1, pessoa2)
        aresta_rota = self.caminho(pessoa1, pessoa2)

        G = nx.Graph(self.grafo)
        # Calcula a posição dos nós uma única vez para que tudo fique alinhado
        pos = nx.spring_layout(G)

        # Camada 1: Vertices e as arestas de fundo
        nx.draw_networkx_nodes(G, pos, node_color='lightblue')
        nx.draw_networkx_edges(G, pos, edge_color='gray')

        # Camada 2: Nomes
        nx.draw_networkx_labels(G, pos)

        # Camada 3: Arestas do caminho por cima
        nx.draw_networkx_edges(G, pos, edgelist=aresta_rota, edge_color='red', width=2)

        plt.show()

    def verificacao(self, pessoa1, pessoa2):
        if pessoa1 not in self.grafo or pessoa2 not in self.grafo:
            print(f'{pessoa1} ou {pessoa2} não existe na lista de amigos.')
            exit()

    def mais_popular(self):
        if not self.grafo:
            print(f'{self} está vazia')
            return []

        aux_mais_popular = []
        aux = 0

        for grafo in self.grafo:
            aux_contagem = len(self.grafo[grafo])
            if aux_contagem > aux:
                aux = aux_contagem
                aux_mais_popular = [grafo]
            elif aux == aux_contagem:
                aux_mais_popular.append(grafo)

        return aux_mais_popular

    def visualizar_mais_popular(self):
        mais_populares = self.mais_popular()
        plt.title('Grafo com nós mais populares destacados')

        G = nx.DiGraph(self.grafo)
        pos = nx.spring_layout(G)

        # Cores para os nós
        cores_nos = ['lightblue' if no not in mais_populares else 'yellow' for no in G.nodes()]

        nx.draw(G, pos, with_labels=True, node_color=cores_nos, edge_color='gray', arrows=False)
        plt.show()
