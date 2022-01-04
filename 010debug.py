from collections import defaultdict
#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    hmap=defaultdict(list)
    flag={}
    for i in graph:
        hmap[i[0]].append(i[1])
        hmap[i[1]].append(i[0])
        flag[i[0]]=0
        flag[i[1]]=0
    def safe(ind,col):
        for i in hmap[ind]:
            if(flag[i]==col):
                return(False)
        return(True)
    def helper(flag):
        for ind in flag:
            if(flag[ind]==0):
                for col in range(1,k+1):
                    if(safe(ind,col)):
                        flag[ind]=col
                        if(helper(flag)):
                            return(True)
                        else:
                            flag[ind]=0
                return(False)
        return(True)
    if(helper(flag)):
        return(1)
    else:
        return(0)
graph=[(0,1),(1,2),(0,2)]
k=3
v=len(graph)
print(graphColoring(graph,k,v))