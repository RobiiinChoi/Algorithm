graph = {
    0 : [1, 4],
    1 : [0, 2, 3, 4],
    2 : [1, 3],
    3 : [1, 2, 4],
    4 : [0, 1, 3]
}


class Solution:

    # Function to return the adjacency list for each vertex.
    def printGraph(self, V, adj):
        myAdj=[]
        for i in range(V):
            myAdj.append([i])
        for i in range(V):
            index = adj[i]
            for num in index:
                myAdj[i].append(num)

        return myAdj
