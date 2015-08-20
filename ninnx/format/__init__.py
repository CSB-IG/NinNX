def Net2Infomap(red,sep,form):
    """
    rewrites network from txt to infomap format
    """
  
    Red = GetNetX(red,sep,form)
    genesDIC = Red[1]
    G = Red[0]
  
    name = red.split('.')
    output = name[0]+'.net'
    SALIDA = open(output,"w")

    SALIDA.write("%s %s \n" % ("*Vertices", len(genesDIC)))
    
    i = 1
    for n in genesDIC:
        SALIDA.write('%s "%s" \n' % (i,n))
        i+=1
  
    SALIDA.write("%s %s \n" % ("*Edges", G.number_of_edges()))
  
    for e in G.edges():
        ed = G.get_edge_data(*e)
        SALIDA.write("%s %s %s \n" % (e[0],e[1],ed['w']))
    
    SALIDA.close()
