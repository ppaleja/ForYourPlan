#Python program to print topological sorting of a DAG 
from collections import defaultdict 

#Class to represent a graph 
class Graph: 
	def __init__(self,vertices): 
		self.graph = defaultdict(list) #dictionary containing adjacency List 
		self.V = vertices #No. of vertices 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# A recursive function used by topologicalSort 
	def topologicalSortUtil(self,v,visited,stack): 

		# Mark the current node as visited. 
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		# Push current vertex to stack which stores result 
		stack.insert(0,v) 

	# The function to do Topological Sort. It uses recursive 
	# topologicalSortUtil() 
	def topologicalSort(self): 
		# Mark all the vertices as not visited 
		visited = [False]*self.V 
		stack =[] 

		# Call the recursive helper function to store Topological 
		# Sort starting from all vertices one by one 
		for i in range(self.V): 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		# Print contents of stack 
		print(stack)

# NOTE: This code is copied directly from https://www.geeksforgeeks.org/python-program-for-topological-sorting/
# 
# The above class is an implementation of the graph data structure. This
# graph will hold a vertex for each class that we are considering. For example,
# the string "CSE 20" will be its own vertex. To create the edges of this graph,
# we will use the prerequisite data scraped from easyCAPEs. For each GET request
# to easyCAPEs, we will see a list of prerequisites. We need to represent each
# of those prerequsite class-corresponding class relationships as an edge in the
# graph. For example, CSE 100 has CSE 30 and CSE 21 as prerequisites. Therefore,
# we need an edge from CSE 30 to CSE 100 and another edge from CSE 21 to CSE 100.

# TODO: Replace the argument with the number of vertices (classes)
g= Graph(6)

# TODO: Create a for loop that adds an edge from a prerequisite to its corresponding class.
#  - arg1: prerequisite class; in the form of a string (e.g. "CSE 30")
#  - arg2: class that follows prerequisite; again, in the form of a string (e.g. "MATH 180A")
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 

print("Following is a Topological Sort of the given graph")
g.topologicalSort() 
#This code is contributed by Neelam Yadav
