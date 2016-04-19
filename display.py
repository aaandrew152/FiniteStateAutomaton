import networkx as nx
import matplotlib.pyplot as plt

def graphics(strats,number,prevalence):


    # THIS DOESNT ALLOW TWO ARROWS GOING FROM AND TO THE SAME PLACES (which we need for different conditions)
    G = nx.DiGraph()

    colours = ['blue' if x[1] == 0 else 'red' for x in strats]
    edge_col = []

    for state,strat,arrows in strats:

        G.add_node(state)

        # add arrows
        for arrow in arrows:
            if arrow:
                if not state == arrow[0]:
                    G.add_edge(state,arrow[0])
                    edge_col.append('blue' if arrow[1][0] == 0 else 'red')

    #pos = dict([(i,(i,0)) for i in G.nodes()])

    plt.figure('Strategy ' + str(number))
    nx.draw(G, node_color = colours, edge_color = edge_col)
    plt.savefig('simulations/strategy' + str(number) + '_' + str(prevalence) + '%.png')
    plt.show()

# get and count the different strategies        
def display(individualList):

    strats = []

    for player in individualList:

        new_strat = player.getStratNumbers()
        flag = 0

        if not strats:
            strats.append((new_strat,1))

        else:
            for idx,(strat,count) in enumerate(strats):
                if new_strat == strat:
                    strats[idx] = (strat,count+1)
                    flag = 1

            if flag == 0:
                strats.append((new_strat,1))

    for idx, (strat,count) in enumerate(strats):
        print('Strategy ' + str(idx + 1) + ': ' + str(strat) + ', Prevalence: ' + str (count/len(individualList) * 100) + '% \n')
        graphics(strat,idx+1,count/len(individualList) * 100)


# insert code for graphical output here