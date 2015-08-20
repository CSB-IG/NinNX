
def GetNetX(red,sep,form):
    diccionario = {}
    genesDIC = []
    G = nx.Graph()

    sep = separador(sep)
    
    interacciones = open(red).readlines()

    k = 1
    tmp="---"
    for i in interacciones:
        genes  = i.split(sep)

        a=genes[0].strip()
        b=genes[1].strip()
        c=genes[2].strip()
      
        if (form == "nIn"):
            if (genes[0].strip() not in genesDIC): genesDIC.append(genes[0].strip())
            if (genes[2].strip() not in genesDIC): genesDIC.append(genes[2].strip())

	
        elif (sep == "nnI"):      
            if (genes[0].strip() not in genesDIC): genesDIC.append(genes[0].strip())
            if (genes[1].strip() not in genesDIC): genesDIC.append(genes[1].strip())

	
    i = 1
    for n in genesDIC:
        diccionario[n] = i
        #SALIDA.write('%s "%s" \n' % (i,n))
        i+=1

      
    for i in interacciones:
        campos  = i.split(sep)

        a=campos[0].strip()
        b=campos[1].strip()
        c=campos[2].strip()
      
        if (form == "nIn"):
            if (b == "pp"):
                b = 1
        else:
            b=float(b)
            if (a in diccionario and c in diccionario):
                if (diccionario[a] == diccionario[c]):
                    G.add_node(diccionario[a])
            else:
                if ((G.has_edge(diccionario[a],diccionario[c]) == False) and (G.has_edge(diccionario[c],diccionario[a]) == False)):
                    G.add_edge(diccionario[a],diccionario[c],w=b)
        
                elif (sep == "nnI"):
                    if (c == "pp"):
                        c = 1
                    else:
                        c=float(c)
                    if (a in diccionario and b in diccionario):
                        if (diccionario[a] == diccionario[b]):
                            G.add_node(diccionario[a])
                        else:
                            if ((G.has_edge(diccionario[a],diccionario[b]) == False) and (G.has_edge(diccionario[b],diccionario[a]) == False)):
                                G.add_edge(diccionario[a],diccionario[b],w=c)
        

    return G,genesDIC






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











    

def Net2AdjMatrix(red,sep,form):
    Red = GetNetX(red,sep,form)
    genesDIC = Red[1]
    G = Red[0]
    sep = separador(sep)
  
    name = red.split('.')
    output = name[0]+'.txt'
    SALIDA = open(output,"w")  
  
  
    nodes = []

    for i in G.nodes():
        nodes.append(genesDIC[i-1])

  
    Q = nx.to_numpy_matrix(G,weight='w')  
  
    SALIDA.write(sep)  
    for i in nodes:
        SALIDA.write(("%s"+sep) % i)  
    SALIDA.write("\n")  

    for i in range(len(Q)):
        SALIDA.write(("%s"+sep) %  nodes[i])  
        for j in range(len(Q)):
            SALIDA.write(("%s"+sep) %  Q.item((i,j)))     
            SALIDA.write("\n")

    SALIDA.close()









def write_adj_matrix( path, g ):
    with open(path, 'w') as out:
        a = nx.adjacency_matrix(g).toarray()

        nodes = g.nodes()
        
        out.write("\t".join(['x',] + [n for n in nodes] ) + "\n")
    
        for row in a:
            line = [nodes.pop(0),] + list([str(int(i)) for i in row])
            out.write("\t".join(line) + "\n")
            
