from libKosaraju import Graph

g = Graph(5)
g.join(1,0)
g.join(0,2)
g.join(2,1)
g.join(0,3)
g.join(3,4)
print(g.graph)
print(g.transpose().graph)

g.returnSCCs()