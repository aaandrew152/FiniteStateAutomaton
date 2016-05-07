import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

G = nx.DiGraph()

strats = [(0, 1, [(1, [1])]), (1, 0, [(0, [0])]),(2,1,[None])]

colours = [None]*len(strats)
edge_col = []

for state,strat,arrows in strats:

	G.add_node(state)

	# set state colour
	if strat == 0:
		colours[state] = 'blue'
	else:
		colours[state] = 'red'

	# add arrows
	for arrow in arrows:
		if arrow:
			G.add_edge(state,arrow[0])
			edge_col.append('blue' if arrow[1][0] == 0 else 'red')

pos = dict([(i,(i,0)) for i in G.nodes()])
label = {(0,1):'1',(1,0):'12'}
nodes = {0:'*',1:'',2:''}

plt.figure('Strat 1')
nx.draw(G, pos, labels = nodes, node_color = colours, edge_color = edge_col)
#nx.draw_networkx_labels(G,pos,nodes)
nx.draw_networkx_edge_labels(G,pos,edge_labels = label)
# plt.savefig('images1/fsa.png')
plt.show()


# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib.patches import FancyArrowPatch, Circle
# import numpy as np

# def draw_network(G,pos,ax,sg=None):

#     for n in G:
#         c=Circle(pos[n],radius=0.02,alpha=0.5)
#         ax.add_patch(c)
#         G.node[n]['patch']=c
#         x,y=pos[n]
#     seen={}
#     for (u,v,d) in G.edges(data=True):
#         n1=G.node[u]['patch']
#         n2=G.node[v]['patch']
#         rad=0.1
#         if (u,v) in seen:
#             rad=seen.get((u,v))
#             rad=(rad+np.sign(rad)*0.1)*-1
#         alpha=0.5
#         color='k'

#         e = FancyArrowPatch(n1.center,n2.center,patchA=n1,patchB=n2,
#                             arrowstyle='-|>',
#                             connectionstyle='arc3,rad=%s'%rad,
#                             mutation_scale=10.0,
#                             lw=2,
#                             alpha=alpha,
#                             color=color)
#         seen[(u,v)]=rad
#         ax.add_patch(e)
#     return e


# G=nx.MultiDiGraph([(1,2),(1,2),(2,3),(3,4),(2,4),
#                 (1,2),(1,2),(1,2),(2,3),(3,4),(2,4),(1,3),(2,5)]
#                 )

# pos=nx.spring_layout(G)
# ax=plt.gca()
# draw_network(G,pos,ax)
# ax.autoscale()
# plt.axis('equal')
# plt.axis('off')
# plt.show()