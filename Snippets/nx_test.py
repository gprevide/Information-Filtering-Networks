# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:06:06 2020

@author: Guido Previde Massara

Abstract:
	Some examples on planarity, chordality and drawing of clique forests

"""
import networkx as nx
import matplotlib.pyplot as plt
g = nx.Graph()
g.add_nodes_from(range(1,6))

c1 = nx.complete_graph(range(1,5))
c2 = nx.complete_graph(range(3,7))
c3 = nx.complete_graph(list([1,7]))

print(c1.edges)

ct = nx.Graph()
ct.add_edges_from(c1.edges)
ct.add_edges_from(c2.edges)
ct.add_edges_from(c3.edges)


is_planar, ignore = nx.check_planarity(ct, counterexample=False)
is_chordal = nx.is_chordal(ct)

tree = nx.maximum_spanning_tree(ct)

print(f"Graph is planar {is_planar}, is chordal {is_chordal}")

plt.subplot(211)
nx.draw(ct)
plt.subplot(221)
nx.draw(tree)