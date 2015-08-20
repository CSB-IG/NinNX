import networkx as nx

def NetStats(G):
    return { 'radius': nx.radius(G),
             'diameter': nx.diameter(G),
             'connected_components': nx.number_connected_components(G),
             'density' : nx.density(G),
             'shortest_path_length': nx.shortest_path_length(G),
             'clustering': nx.clustering(G)}
