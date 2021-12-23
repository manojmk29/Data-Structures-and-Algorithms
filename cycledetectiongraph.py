# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:
    # Constructor
    def __init__(self):

    # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v]
    def havecycle(self):
        aa=max(list(self.graph.keys()))
        bag=[False]*(int(aa)+1)
        jk=list(self.graph.keys())
        for i in jk:
            if(self.cycle_help(i,bag)==True):
                return(True)
        return(False)
    def cycle_help(self,node,bag):
        if(bag[node]==True):
            return(True)
        else:
            bag[node]=True
        for i in self.graph[node]:
            if(self.cycle_help(i,bag)==True):
                return(True)
        bag[node]=False
        return(False)
g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
# g.addEdge(3, 0)   
# print(g.BFS(2))
print(g.havecycle())