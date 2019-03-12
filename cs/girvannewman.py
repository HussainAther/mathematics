import networkx as nx
import math
import csv
import random as rand
import sys

"""
Run using:

"python girvannewman.py cgraph.dat"

or replace "cgraph.dat" with whatever graph file you want.

The Girvan–Newman algorithm (named after Michelle Girvan and Mark Newman) is a hierarchical
method used to detect communities in complex systems. It constructs a graph by detecting communities
in the network.

The steps are generally:
1. The betweenness of all existing edges in the network is calculated first.
2. The edge with the highest betweenness is removed.
3. The betweenness of all edges affected by the removal is recalculated.
4. Steps 2 and 3 are repeated until no edges remain.
"""

def buildG(G, file_, delimiter_):
    """
    Build a graph from the cgraph.dat file or whatever input file is given.
    """
    reader = csv.reader(open(file_), delimiter=delimiter_)
    for line in reader:
        if len(line) > 2:  # for the format of cgraph.dat
            if float(line[2]) != 0.0: # if there are 3 edges
                G.add_edge(int(line[0]),int(line[1]),weight=float(line[2]))
        else: # 2 edges
            G.add_edge(int(line[0]),int(line[1]),weight=1.0)

def gnStep(g):
    """
    Perform the steps of the algorithm
    """
    init_ncomp = nx.number_connected_components(g) # get the number of components
    ncomp = init_ncomp # initialize with the initial number of components
    while ncomp <= init_ncomp: # loop through the steps as the algorithm dictates
        w = nx.edge_betweenness_centrality(g, weight="weight") # centrality of the edges
        themax = max(bw.values()) # max
        for k, v in bw.iteritems():
            if float(v) == themax: # if that edge is the maximum
                g.remove_edge(k[0], k[1]) # remove that edge
        ncomp = nx.number_connected_components(g) # recalcualte and perform the algorithm again

def gnModularity(g, deg, m):
    """
    Compute modularity of the part of the matrix
    """
    new = nx.adj_matrix(g) # get the adjacency matrix
    dego = Deg(new, g.nodes()) # degree of the matrix
    comps = nx.connected_components(g)
    mod = 0 # modularity of the partition
    for c in comps:
        ewc = 0 # edges in a community
        re = 0 # random edges
        for i in c:
            ewc += dego[i]
            re += deg
        mod += (float(ewc) - float(re**2) / float(2*m)) # modularity of the matrix
    mod = mod/float(2*m)

def Deg(a, nodes):
    """
    Update the degrees of the matrix and return a dictionary of the
    updated nodes.
    """
    dicto = {} # that's spanish for dicto
    b = a.sum(axis=1)
    for i in range(len(nodes)):
        dicto[nodes[i]] = b[i, 0]
    return dicto

