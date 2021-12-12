#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:53:24 2020

@author: xg7
"""



class Graph:
    
    def  __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict
        
    def vertices(self):
        return list(self._graph_dict.keys())
    
    def edges(self):
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    def neighbors(self, v):
        if v in self._graph_dict.keys():
            return self._graph_dict[v]
        else:
            print(v +" is not in the graph.")
    
    
    def add_vertex(self, vertex):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []
        else:
            print(vertex + " has already been in the graph.")
            
            
#    def remove_vertex(self, vertex):
#        if vertex in self._graph_dict:
#            edges = self._graph_dict.pop(vertex)
#            for v in edges:
#                self._graph_dict[v].remove(vertex)
#        else:
#            print(vertex + "is not in the graph.")
            
    def remove_vertex(self, vertex):
        if vertex in self._graph_dict:
            edges = self._graph_dict[vertex][:]
            for v in edges:
                self.remove_edge(vertex, v)
            del(self._graph_dict[vertex])
     
            
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self._graph_dict:
            self._graph_dict[vertex1].append(vertex2)
        else:
            self._graph_dict[vertex1] = [vertex2]
        if vertex2 in self._graph_dict:
            self._graph_dict[vertex2].append(vertex1)
        else:
            self._graph_dict[vertex2] = [vertex1]
            
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self._graph_dict.keys():
           if vertex2 in self._graph_dict[vertex1]:
                self._graph_dict[vertex1].remove(vertex2)
                self._graph_dict[vertex2].remove(vertex1)
                
    

    def __str__(self):
        return "{}".format(self._graph_dict)



def load_graph(file_name):
    graph = {}
    f = open(file_name, "r")
    records = f.readlines()
    for r in records:
        r = r.strip()
        graph[r[0]] = [c for c in r[1:]]
    g = Graph(graph)
    return g
    

def trace_contact(graph, v, component=[]):
    if v not in component:
        component.append(v)
    neighbors = graph.neighbors(v) 
    for n in neighbors:
        if n not in component:
            trace_contact(graph, n, component)
    return component
    
#def dfs(graph, v, component=[]):
#    neighbors = graph.neighbors(v)
#    for n in neighbors:
#        if n not in component:
#            component.append(n)
#            dfs(graph, n, component)
#    return component
            
if __name__ == "__main__":
    fig1 = {"a":["b", "c", "d"],
                "b":["a", "d"],
                "c":["a", "d"],
                "d":["a", "b","c"],
                "e":["f"],
                "f":["e"]}
    
##---When DO_ALL_TEST = False, You can manually test your code 
##---in the console one by one,like the given examples.
##---If you want to run all the tests together,
##---Please set DO_TEST = True ---##
    DO_ALL_TEST = True
    if DO_ALL_TEST:
        graph_fig1 = Graph(fig1)
        print("--------Tests of Q2(a)--------")
        print()
        print("---Testing:---\n graph_fig1.vertices()\n", graph_fig1.vertices())
        print()
        print("---Testing:---\n graph_fig1.neighbors('a')\n", graph_fig1.neighbors("a"))
        print()
        print("---Testing:---\n graph_fig1.neighbors('z')")
        graph_fig1.neighbors("z")
        print()
        print("---Testing:---\n graph_fig1.edges()\n", graph_fig1.edges())
        print()
        print("---Testing:---\n graph_fig1.add_vertex('g')\n")
        graph_fig1.add_vertex("g")
        print(graph_fig1.vertices())
        print()
        print(" graph_fig1.add_vertex('a')")
        graph_fig1.add_vertex("a")
        print()
        print("---Testing:---\n graph_fig1.add_edge('d', 'e')\n")
        graph_fig1.add_edge("d", "e")
        print(" graph_fig1.edges()")
        print(graph_fig1.edges())
        print()
        print("---Testing:---\n graph_fig1.add_edge('f', 'g')")
        print("Note: vertex 'g' is not in the edge")
        graph_fig1.add_edge("f", "g")
        print(" graph_fig1.edges()")
        print(graph_fig1.edges())
        print()   
        print("---Testing:---\n graph_fig1.remove_edge('f', 'g')\n")
        graph_fig1.remove_edge("f", "g")
        print(" graph_fig1.edges()")
        print(graph_fig1.edges())
        print()
        print("---Testing:---\n graph_fig1.remove_edge('d', 'e')\n")
        graph_fig1.remove_edge("d", "e")
        print(" graph_fig1.edges()")
        print(graph_fig1.edges())
        print()
        print("---Testing:---\n graph_fig1.remove_edge('d', 'g')\n")
        graph_fig1.remove_edge("d", "g")
        print(" graph_fig1.edges()")
        print(graph_fig1.edges())
        print()
        print("---Testing:---\n graph_fig1.remove_vertex('g')\n")
        print("When 'g' is an isolate vertex" )
        graph_fig1.remove_vertex("g")
        print(" graph_fig1.vertices()")
        print(graph_fig1.vertices())
        print(" graph_fig1.edges()")
        print(graph_fig1.edges())
        print()
        print("---Testing:---\n graph_fig1.remove_vertex('a')\n")
        graph_fig1.remove_vertex("a")
        print(" graph_fig1.vertices()")
        print(graph_fig1.vertices())
        print(" graph_fig1.edges()")
        print(graph_fig1.edges())
        print() 
        print("---Testing:---\n graph_fig1.remove_vertex('z')\n")
        print("When 'z' is not in the graph,")
        graph_fig1.remove_vertex("z")
        print(" graph_fig1.vertices()")
        print(graph_fig1.vertices())
        print() 
        print("---Tests of Q2(b)---")
        graph_fig2 = load_graph("contacts.txt")
        print("The fig2 is loaded\n")
        print(graph_fig2)
        component = []
        print("The contacts of node a:\n", trace_contact(graph_fig2, "a", component))
        print("After adding an edge {d, e},")
        if graph_fig2 != None:
            graph_fig2.add_edge("d", "e")
        component = []
        print("The contacts of node a:\n", trace_contact(graph_fig2, "a", component))
        
    
    
    