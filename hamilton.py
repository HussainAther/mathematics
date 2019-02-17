"""
Validate and draw Hamilton graphs and paths
"""

graph = {'1': ['2', '4','5'],
             '2': ['1', '3','5'],
             '3': ['2','5','6'],
             '4': ['1','7','5'],
             '5': ['1','2','3', '4','6','7','8','9'],
             '6': ['3','5','9'],
             '7': ['4','5','8'],
             '8': ['7','5','9'],
             '9': ['8','5','6']}

def find_all_paths(graph, start, end, path=[]):
        #http://www.python.org/doc/essays/graphs/
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
def find_paths(graph):
    cycles=[]
    for startnode in graph:
        for endnode in graph:
            newpaths = find_all_paths(graph, startnode, endnode)
            for path in newpaths:
                if (len(path)==len(graph)):
                    cycles.append(path)
    return cycles

def find_cycle(graph):
    cycles=[]
    for startnode in graph:
        for endnode in graph:
            newpaths = find_all_paths(graph, startnode, endnode)
            for path in newpaths:
                if (len(path)==len(graph)):
                    if path[0] in graph[path[len(graph)-1]]:
                        #print path[0], graph[path[len(graph)-1]]
                        path.append(path[0])
                        cycles.append(path)
    return cycles

print "Finding Hamiltonian Paths----"

a= find_paths(graph)
##for any in a:
##    for d in any:
##        print d, "->",
##    print
print "Number of Hamiltonian Paths=", len(a)
print "Finding Hamiltonian Cycles----"
a= find_cycle(graph)
##if (a ==[]):
##    print "No Hamiltonian Cycle"
##else:
##    for any in a:
##        for d in any:
##            print d, "->",
##        print

print "Number of Hamiltonian Cycles=", len(a)
#Visualize
# http://ashitani.jp/gv/
G=graph
f = open('dotgraph.txt','w')
f.writelines('digraph G {\nnode [width=.3,height=.3,shape=octagon,style=filled,color=skyblue];\noverlap="false";\nrankdir="LR";\n')
f.writelines
for i in G:
    for j in G[i]:
        s= '      '+ i
        s +=  ' -- ' +  j
        s+=';\n'
        f.writelines(s)
        G[j].remove(i)


f.writelines('}')
f.close()
print "done!"
