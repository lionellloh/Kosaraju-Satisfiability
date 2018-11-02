class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = dict()
        self.store = []
        self.big_store = []

    def join(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)

        else:
            self.graph[u] = [v]

    def DFSUtil(self, v, visited):
        visited[v] = True
        self.store.append(v)
        # print(v, end=",")


        # Make sure it is non null
        if self.graph.get(v, None):
            for neighbour in self.graph[v]:
                if not visited[neighbour]:
                    self.DFSUtil(neighbour, visited)


    def fillStack(self, stack, i, visited):

        visited[i] = True

        for j in self.graph.get(i, []):
            if not visited[j]:
                self.fillStack(stack, j, visited)

        stack = stack.append(i)


    def transpose(self):
        g = Graph(self.vertices)
        for i in self.graph:
            for j in self.graph[i]:
                g.join(j, i)

        return g


    def returnSCCs(self):


        stack = []
        #Initialise with all false values first

        # Initialize visit_records

        visited = [False] * self.vertices

        for i in range(0, self.vertices):

            if not visited[i]:
                self.fillStack(stack, i, visited)

        g_transposed = self.transpose()

        visited = [False] * self.vertices

        while stack:
            i = stack.pop()
            if not visited[i]:

                g_transposed.DFSUtil(i, visited)
                # print("")
                self.big_store.append(g_transposed.store)
                g_transposed.store = []

        return(self.big_store)
















