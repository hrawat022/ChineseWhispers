'''
Created on Apr 3, 2013

@author: Sanmaya Jolly
'''

from graph import Graph
from cluster import Cluster
from graphmanip import *
from clustermanip import random_cluster, probabilistic_best_cluster
from ioaux import file_input_test_data as input_from_file

if __name__ == '__main__':
    g = Graph()
    g = input_from_file()
    clustersli = []
    mode = 0
    print "1. Random\n2. Probabistic"
    mode = int(raw_input())
    for node_name in g.graf.nodes():
        newclusters = get_max_weighted_clusters(g, node_name)
        if mode == 1:
            newcluster_name = random_cluster(newclusters)
        else:
            newcluster_name = probabilistic_best_cluster(g.graf.node[node_name], newclusters)
        #print "Node:", node_name, "Newcluster:", newcluster_name
        if newcluster_name:
            found = False
            for c in clustersli:
                if c.label == newcluster_name:
                    c.add_node(node_name)
                    found = True
                    break
            if not found:
                c = Cluster(ID = newcluster_name)
                c.add_node(node_name)
                clustersli.append(c)
            change_node_cluster(g, node_name, c.label)
        else:
            c = Cluster(ID = node_name)
            c.add_node(node_name)
            clustersli.append(c)
    for c in clustersli:
        print c.label, c.node_list, c.strength()
    