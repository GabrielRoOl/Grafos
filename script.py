import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

grafo_amigos = {
    "Gabriel": ["Taynara", "Jhonatan", "Jeferson"],
    "Taynara": ["Aline", "Jhonatan"],
    "Aline": ["Jhonatan", "Taynara"],
    "Jhonatan": ["Gabriel", "Taynara", "Aline"],
}


def adicionar_pessoas(grafo, nome):
    """
    Adiciona uma pessoa ao grafo, se ela ainda não existir.
    - grafo: o nosso array de amigos
    - nome: o nome da pessoa que vai ser adicionada
    """
    if nome not in grafo:
        grafo[nome] = []
    else:
        print(f"{nome} já existe na rede de amigos.")


def adicionar_amizade(grafo, pessoa1, pessoa2):
    """
    Adiciona uma nova amizade entre duas pessoas
    Uma amizade é uma via de mão dupla, por isso adicionamos a conexão nos dois sentidos.
    """
    if pessoa1 in grafo and pessoa2 in grafo:
        if pessoa1 in grafo[pessoa2] or pessoa2 in grafo[pessoa1]:
            print(f"{pessoa1} e {pessoa2} já são amigos.")
            return
        if pessoa1 not in grafo[pessoa2]:
            grafo[pessoa2].append(pessoa1)

        if pessoa2 not in grafo[pessoa1]:
            grafo[pessoa1].append(pessoa2)

    else:
        print(f"Uma ou ambas as pessoas não existem na lista de amigos.")


def sugerir_amigos(grafo, nome):
    """
    Mostra uma lista de amigos a partir dos amigos dessa pessoa
    """
    print(f'\nSugestão de amigos para {nome}: ')
    if nome not in grafo:
        print(f"{nome} não está cadastrado.")
        return
    amigos = grafo[nome]

    resultado = []

    for amigo_direto in amigos:
        amigos_dos_amigos = grafo[amigo_direto].copy()
        if nome in amigos_dos_amigos:
            amigos_dos_amigos.remove(nome)

        resultado.extend(amigos_dos_amigos)

    lista_final = list(dict.fromkeys(resultado))
    print(lista_final)


adicionar_pessoas(grafo_amigos, "João")
adicionar_pessoas(grafo_amigos, "Ana")
adicionar_pessoas(grafo_amigos, "Beto")
adicionar_pessoas(grafo_amigos, "Jeferson")
adicionar_pessoas(grafo_amigos, "Nelson")
adicionar_pessoas(grafo_amigos, "Amanda")

adicionar_amizade(grafo_amigos, "Ana", "Taynara")
adicionar_amizade(grafo_amigos, "João", "Beto")
adicionar_amizade(grafo_amigos, "Gabriel", "Beto")
adicionar_amizade(grafo_amigos, "João", "Ana")
adicionar_amizade(grafo_amigos, "Nelson", "Amanda")
adicionar_amizade(grafo_amigos, "Taynara", "Amanda")

plt.title("Grafo Amigos")

G = nx.Graph(grafo_amigos)
rota = nx.shortest_path(G, "Nelson", "Jeferson")

aresta_rota = []

for i in range(len(rota) - 1):
    aresta = (rota[i], rota[i + 1])
    aresta_rota.append(aresta)

pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
nx.draw_networkx(G, pos, with_labels=True, edgelist=aresta_rota, node_color="yellow", edge_color="red", width=2)
print(aresta_rota)
plt.show()
