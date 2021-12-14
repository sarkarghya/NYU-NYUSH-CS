#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:53:24 2020

@author: xg7
"""


##---Q1(a)----##

class Graph:
    
    def  __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict
        
    def vertices(self):
        """
        This method returns a list of vertices.
        """
        ##---start your code here---##
        
    
        return 
        ##---end of your code---##
        
    def neighbors(self, v):
        """
        This method returns a list of vertices that 
        connect with v by one edge.
        """
        ##---start your code here---##
    
       
        return 
        
        ##---end of your code---##
        
    def edges(self):
        """
        This method returns a list of edges.
        """
        ##---start your code here---##
    
       
        return 
        ##---end of your code---##
        
    
    def add_vertex(self, vertex):
        """
        This method adds the vertex into the graph.
        """
        ##---start your code here---##
         
        pass
    
        ##---end of your code---##
        
            
    def add_edge(self, vertex1, vertex2):
        """
        This method adds the edge {vertex1, vertex2} 
        into the graph.
        """
        ##---start your code here---##
         
        pass
    
        ##---end of your code---##
    
    def remove_edge(self, vertex1, vertex2):
        """
        This method reomves the edge {vertex1, vertex2} 
        in the graph.
        """
        ##---start your code here---##
        
        
        pass
    
    
        ##---end of your code---##
        
    def remove_vertex(self, vertex):
        """
        This method reomves the vertex and 
        the edges containing it from the graph.
        """
        ##---start your code here---##
        
        
        pass
    
    
        ##---end of your code---##
    
    
    def __str__(self):
         return "{}".format(self._graph_dict)



##------Q1(b)------##
    
def load_graph(file_name):
    """
    This function loads the file of contacts and 
    returns an instance of Graph class
    """
    ##---start your code here---##
    
    return 
   ##---end of your code---##
    

def trace_contact(g, v, component=[]):
    """
    This function returns the largest component of v in the graph.
    """
    ##---start your code here---##
    
    
    ##---end of your code---##
    return component
    

##---Tests of your code.----##
##---NOTE:---##  
##---DO_ALL_TESTS is a swith which allows you 
##---to test your code one by one in the console.---##

if __name__ == "__main__":
    fig1 = {"a":["b", "c", "d"],
                "b":["a", "d"],
                "c":["a", "d"],
                "d":["a", "b", "c"],
                "e":["f"],
                "f":["e"]}

##---When DO_ALL_TEST = False, You can manually test your code 
##---in the console one by one,like the given examples.
##---If you want to run all the tests together,
##---Please set DO_ALL_TEST = True ---##
    
    DO_ALL_TESTS = False 
    if DO_ALL_TESTS:
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
    
    
    
    