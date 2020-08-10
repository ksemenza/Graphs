"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # create a dictionary(hashtable) to hold the vertices of the graph
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
    def add_vertex(self, vertex_id):
            # create an empty set to hold vertices
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # add an edge value to the set in each vertex
        self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
         # function to calculate all edges of a vertex
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
          # create a queue (BFT requires a queue)
        q = Queue()
        # enqueue the starting index
        q.enqueue(starting_vertex)
        # create a blank set to hold the nodes that have been visited
        visited = set()

        # run a loop while the queue still has items
        while q.size() > 0:

            # dequeue the first item and store it in a variable
            v = q.dequeue()

            # check if the node has already been visited or not
            if v not in visited:
                # if not, print it and 
                # add it to the set
                print(v)
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    # enqueue new vertices for all the neighbors
                    q.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack (DFT requires a stack)
        s = Stack()
        # push the starting index
        s.push(starting_vertex)
        # create a blank set to hold the nodes that have been visited
        visited = set()

        # run a loop while the stack still has items
        while s.size() > 0:

            # pop the first item and store it in a variable
            v = s.pop()

            # check if the node has already been visited or not
            if v not in visited:
                # if not, print it and 
                # add it to the set
                print(v)
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    # push new vertices for all the neighbors
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # base case:
        # if visited doesn't exist, create a new set
        # and add the starting vertex
        if not visited:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)

        # loop through all the vertices,
        # and if it hasn't been visited,
        # recursively call DFT
        for vert in self.vertices[starting_vertex]:
            if vert not in visited:
                self.dft_recursive(vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
         # create a queue (BFS requires a queue)
        # and enqueue the starting vertex in a list (to keep track of the traveled path)
        # create a visited set to keep track of visited nodes
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        # while the queue still has items
        while q.size() > 0:
            # grab the first item in the queue
            path = q.dequeue()
            # and grab the vertex from the last index in the path
            vert = path[-1]

            # if the vertex hasn't been visited
            if vert not in visited:

                # if the vertex equals our destination value,
                # return the path, we have our answer
                if vert == destination_vertex:
                    return path

                # else add the vertex to visited
                visited.add(vert)

                # loop through all remaining neighbors and
                # create a copy of the path,
                # append the new vertex for all neighbors to the path,
                # and enqueue the new paths
                for next_vert in self.get_neighbors(vert):
                    path_copy = list(path)
                    path_copy.append(next_vert)
                    q.enqueue(path_copy)

        # if we get here, there was no path from start to destination
        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
         # create a Stack (DFS requires a stack)
        # and push the starting vertex in a list (to keep track of the traveled path)
        # create a visited set to keep track of visited nodes
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        # while the stack still has items
        while s.size() > 0:
            # grab the first item in the stack
            path = s.pop()
            # and grab the vertex from the last index in the path
            vert = path[-1]

            # if the vertex hasn't been visited
            if vert not in visited:

                # if the vertex equals our destination value,
                # return the path, we have our answer
                if vert == destination_vertex:
                    return path

                # else add the vertex to visited
                visited.add(vert)

                # loop through all remaining neighbors and
                # create a copy of the path,
                # append the new vertex for all neighbors to the path,
                # and push the new paths
                for next_vert in self.get_neighbors(vert):
                    path_copy = list(path)
                    path_copy.append(next_vert)
                    s.push(path_copy)

        # if we get here, there was no path from start to destination
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
            # base case
        # if the visited set and the path list are None
        # create new versions,
        # else use the versions passed in as parameters
        if not visited:
            visited = set()
        if not path:
            path = []

        # add the starting vertex to the visited set,
        # and add the vertex passed in to any vertices already in the list
        visited.add(starting_vertex)
        path = path + [starting_vertex]

        # if the starting vertex and the destination are the same,
        # return the path
        if starting_vertex == destination_vertex:
            return path

        # else loop through all remaining vertices,
        # if the vertex hasn't been visited,
        # call dfs recursive and if there is a path,
        # return it
        for vert in self.vertices[starting_vertex]:
            if vert not in visited:
                path_copy = self.dfs_recursive(vert, destination_vertex, visited, path)
                if path_copy:
                    return path_copy

        # if we get here, there was no path so return None 
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
