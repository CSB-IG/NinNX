NinNX Is Not NX
================


    >>> import networkx as nx
    >>> g = nx.erdos_renyi_graph(30, 0.03)
    
    
    >>> from ninnx.analyxe import NetStats
    >>> NetStats(g)
    >>> BaiscNetStats(g) 

    >>> from ninnx.format import nx2infomap
    >>> nx2infomap(g, '/path/to/infomap.txt')
    
