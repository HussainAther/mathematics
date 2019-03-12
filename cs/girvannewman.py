import networkx as nx
import math
import csv
import random as rand
import sys

"""
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
    # read the graph from cgraph.dat file
    reader = csv.reader(open(file_), delimiter=delimiter_)
    for line in reader:
        if len(line) > 2:
            if float(line[2]) != 0.0: # for the format of cgraph.dat
                G.add_edge(int(line[0]),int(line[1]),weight=float(line[2]))
