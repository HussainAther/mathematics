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
        max_ = max(bw.values()) # max

