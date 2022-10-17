# Librería para colas de prioridad. Se usará para evaluar la función h(n)
from queue import PriorityQueue
from unicodedata import name
# Librería para trabajar con grafos
import networkx as nx
# Libería para plotear
import matplotlib.pyplot as plt
# Librería para hacer animaciones
import matplotlib.animation
# Libería para hace updates parciales en lugar de redibujar todo
from functools import partial

# Creamos el grafo
G = nx.Graph()

# La ruta
path = []

# Switch para saber si la animación ya acabó
finished = False

# Agregamos las aristas con sus pesos

map_labels = {'2': "Enviando datos al servidor",
    '3': "Datos recibidos",
    '4': "Enviando respuesta al cliente",
    '5': "Enviando datos al servidor",
    '6': "Envío finalizado"
}
G.add_edge('3', '2')
G.add_edge('2', '4')
G.add_edge('4', '5')
G.add_edge('5', '3')
G.add_edge('5', '6')

# Esquema para imprimir el grafo en matplotlib
pos = nx.nx_pydot.graphviz_layout(G, prog="dot")

# Colores a usar
cmap = matplotlib.cm.get_cmap('Blues')

ani = None
    
def start_animation(curr):
    global ani
    # Función para actualizar la animación
    def update(i, G, pos, ax):
        # i = frame
        # G => Grafo
        # pos => posición de todos los elementos del grafo
        # ax => Donde se imprime la animación
        # Usamos variables globales
        global path
        global finished
        if finished:
            return
        if i > 0:
            color_map = []
            # Para iluminar el nodo actual
            for node in G:
                if curr[0] == node:
                    color_map.append(cmap(0.5))
                else:
                    color_map.append(cmap(0))
            nx.draw_networkx_nodes(G, pos, node_color=color_map, ax=ax)
    # Configuramos matplotlib
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    plt.axis('off')

    upd = partial(update, G=G, pos=pos, ax=ax)
    # Dibujamos las aristas
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, ax=ax)

    # Dibujamos los nombres de los nodos
    # nx.draw_networkx_labels(G, pos, labels={n: n.name for n in G})
    nx.draw_networkx_labels(G, pos, labels={n: map_labels[n] for n in G})

    # Dibujamos los nombres de las aristas
    nx.draw_networkx_edge_labels(
        G, pos,
        font_color='red'
    )


    # Construimos el generador para poder animar en cada iteración
    # generator = temp()

    # Ejecutamos la animación
    ani = matplotlib.animation.FuncAnimation(fig, upd, repeat=True, interval=0.5, frames=10)


    mng = plt.get_current_fig_manager()
    # mng.full_screen_toggle()

    plt.ion()
    plt.show()

def close():
    plt.close()

def pause(interval):
    plt.pause(interval)

if __name__ == "__main__":
    print("Empieza")
    curr = ['3']
    start_animation(curr)
    print("Cambia a 3")
    curr[0] = '3'
    plt.pause(1)
    print("Cambia a 2")
    curr[0] = '2'
    plt.pause(1)
    print("Cambia a 4")
    curr[0] = '4'
    plt.pause(1)
    print("Cambia a 5")
    curr[0] = '5'
    plt.pause(1)
    print("Cambia a 6")
    curr[0] = '6'
    plt.pause(1)
    input("Press [enter] to continue.")