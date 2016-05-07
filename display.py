import networkx as nx
import matplotlib.pyplot as plt
from Parameters import game, parameters
import os
import shutil

# generate graphical representation of strategies
def graphics(strats,number,prevalence,directory):

    # generate a new graph
    G = nx.DiGraph()

    all_colors = ['blue','red','green','purple','cyan','orange'] # list must be at least as long as the number of possible actions

    colors = [all_colors[x[1]] for x in strats]
    # edge_col = []
    arrow_labels = {}

    for state,strat,arrows in strats:

        # add state to graph
        G.add_node(state)

        # add arrows
        for arrow in arrows:
            if arrow:
                if not state == arrow[0]:
                    edge = (state,arrow[0])
                    G.add_edge(state,arrow[0])
                    # edge_col.append('blue' if arrow[1][0] == 0 else 'red')
                    if edge in arrow_labels:
                        arrow_labels[edge] = arrow_labels[edge] + ',' + str(arrow[1][0])
                    else:
                        arrow_labels[edge] = str(arrow[1][0])


    # pos = dict([(i,(i,0)) for i in G.nodes()])
    pos = nx.spring_layout(G)

    # label the origin node
    labels = {i:('*' if i == 0 else '') for i in G.nodes()}

    # plot the graph
    plt.figure('Strategy ' + str(number))
    nx.draw(G,pos, labels = labels, node_color = colors, font_size = 16)
    nx.draw_networkx_edge_labels(G,pos,edge_labels = arrow_labels)
    
    plt.savefig(directory + 'strategy' + str(number) + '_' + str(prevalence) + '%.png')
    plt.close()
    #plt.show()


# save text output
def export(strats,actionsPlayed,directory):

    f = open(directory + 'summary.txt','w')

    f.write('PARAMETERS OF SIMULATION \n')
    f.write('# of Sets: ' + str(parameters.numSets) + ', # of Generations: ' + str(parameters.numGenerations) + '\n')
    f.write('Payoffs: ' + str(parameters.payoffMatrix) + '\n')
    f.write('Discount Factor: ' + str(parameters.discountFactor) + '\n')
    f.write('Mutation Prob: ' + str(parameters.mutationProb) + '\n')
    f.write('   Add State: ' + str(parameters.mutation_addState) + '\n')
    f.write('   Delete State: ' + str(parameters.mutation_deleteState) + '\n')
    f.write('   Change Arrow: ' + str(parameters.mutation_changeArrow) + '\n')
    f.write('   Change Action: ' + str(1 - parameters.mutation_addState - parameters.mutation_deleteState - parameters.mutation_changeArrow) + '\n')
    f.write('Mutation Prune: ' + str(parameters.mutationPrune) + '\n \n')

    if actionsPlayed:
        f.write('OVERALL ACTIONS PLAYED \n')
        for action in range(0, len(game.payoffMatrix)):
            f.write('Action ' + str(action) + ': ' + str(round(actionsPlayed.count(action)/len(actionsPlayed)*100,3)) + '% \n')
        f.write('\n')

    f.write('INDIVIDUAL STRATEGIES \n')
    idx = 0
    for (strat,count) in strats:
        prevalence = count/(parameters.numSets*2) * 100
        if prevalence > 5:
            f.write('Strategy ' + str(idx + 1) + ': ' + str(strat) + ', Prevalence: ' + str(round(prevalence,3)) + '% \n')
            idx += 1

    f.close()

# get and count the different strategies        
def display(individualList,actionsPlayed,sim=0):

    # generate list of strategies
    strats = []
    for player in individualList:

        player.plan.prune() # prune at the end to allow for full state space exploration
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

    # save text + graphical output
    if parameters.saveOutput:

        # specify directory (clear if already exists)
        header = 'simulations/' if not parameters.directory else parameters.directory
        if os.path.isdir(header) and sim == 0:
            shutil.rmtree(header)
        directory = header + 'sim' + str(sim) + '/'
        os.makedirs(directory)        

        # save text information
        export(strats,actionsPlayed,directory)

        # save graphical output
        idx = 0
        if parameters.withGraphics:
            for (strat,count) in strats:
                prevalence = count/len(individualList) * 100
                if prevalence > parameters.prevalence:
                    graphics(strat,idx+1,prevalence,directory) # generate graphical output
                    idx += 1

    # otherwise display to terminal
    else:
        # display overall actions played
        if actionsPlayed:
            print('OVERALL ACTIONS PLAYED')
            for action in range(0, len(game.payoffMatrix)):
                print('Action ' + str(action) + ': ' + str(round(actionsPlayed.count(action)/len(actionsPlayed)*100,3)) + '%')
            print('\n')

        # display prevalence of individual strategies
        print('INDIVIDUAL STRATEGIES')
        idx = 0
        for (strat,count) in strats:
            prevalence = count/len(individualList) * 100
            if prevalence > parameters.prevalence:
                print('Strategy ' + str(idx + 1) + ': ' + str(strat) + ', Prevalence: ' + str(round(prevalence,3)) + '%')
                idx += 1
