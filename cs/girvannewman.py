import networkx as nx
import math
import csv
import random as rand
import sys

"""
The Girvan–Newman algorithm (named after Michelle Girvan and Mark Newman) is a hierarchical
method used to detect communities in complex systems.
"""

def buildG(G, file_, delimiter_):
    # read the graph from cgraph.dat file
    reader = csv.reader(open(file_), delimiter=delimiter_)
    for line in reader:
        if len(line) > 2:
            if float(line[2]) != 0.0: # for the format of cgraph.dat
                G.add_edge(int(line[0]),int(line[1]),weight=float(line[2]))
