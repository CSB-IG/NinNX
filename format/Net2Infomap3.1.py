
import sys
import pylab as pl
import matplotlib.pyplot as plt
import networkx as nx

path = sys.argv[1]
sep = sys.argv[2]
form = sys.argv[3]
D = nx.Graph()



#print sep
#print form

if (sep == "cma"):
  sep = ","
elif (sep == "tab"):
  sep = "\t"
elif (sep == "spa"):
  sep = " "  

interacciones = open(path).readlines()




for i in interacciones:
    campos  = i.split(sep)
    #print campos

    a=campos[0].strip()
    b=campos[1].strip()
    c=campos[2].strip()
  
    #print a,b,c  
  
    if (form == "nIn"):
      if (b == "pp"):
	b = 1
      else:
	b=float(b)
      D.add_edge(a,c,w=b)  
    
    elif (sep == "nnI"):
      if (c == "pp"):
	c = 1
      else:
	c=float(c)
      D.add_edge(a,b,w=c) 
  
  
diccionario = {}

print "*Vertices", D.number_of_nodes()

i = 1
for n in D.nodes():
    diccionario[n] = i
    print '%s "%s"' % (i,n)
    i+=1



G = nx.Graph()

#l = 1
for e in D.edges():
    a,b = e
    ed = D.get_edge_data(*e)
    #print l,a,b
    #l=l+1
  
    #if (a in diccionario and b in diccionario) and (diccionario[a] != diccionario[b]): ## quita interacciones consigo mismo
    #if (a in diccionario and b in diccionario) and (diccionario[a] == diccionario[b]):    
    #if (a in diccionario and b in diccionario):
    if (a in diccionario and b in diccionario) and (diccionario[a] != diccionario[b]):    
      #if (form == "nIn"):
	G.add_edge(diccionario[a],diccionario[b],w=ed['w'])
      #elif (sep == "nnI"):
	#G.add_edge(diccionario[a],diccionario[b],w=ed['w'])
	#print diccionario[a],diccionario[b]

    #if (form == "nIn"):
      #b=float(b)
      #D.add_edge(a,c,w=b)  
    
    #elif (sep == "nnI"):
      #c=float(c)
      #D.add_edge(a,b,w=c) 
  	
    
print "*Edges", G.number_of_edges()
for e in G.edges():
    #print e
    ed = G.get_edge_data(*e)
    #print ed
    #print "%s,%s,%s" % (e[0],e[1],ed['w'])
    print "%s %s %s" % (e[0],e[1],ed['w']) 


#A = nx.adjacency_matrix(G)

#for i in range(len(A)):
  #print A[i]

#print A
