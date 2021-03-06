'''
Created on Apr 3, 2013

@author: Sanmaya Jolly
'''

#from graph import Graph
#import networkx as nx
import clusterglobals
from clustermanip import random_cluster
from clusterglobals import replace_cluster, get_cluster

def get_max_weighted_edges(graph, node_name):
    maxw = 0
    maxl = []
    for n, nbrs in graph.graf.adjacency_iter():
        if n == node_name:
            for nbr, eattr in nbrs.items():
                weight = eattr['weight']
                if weight > maxw:
                    maxw = weight
                    maxl = [(nbr, graph.graf.node[nbr]['CLID'])]
                elif weight == maxw:
                    maxl.append((nbr, graph.graf.node[nbr]['CLID']))
    return (maxw, maxl)


def change_node_cluster(graph, node_name, new_label):
    old_label = graph.graf.node[node_name]['CLID']
    graph.graf.node[node_name]['CLID'] = new_label
    return old_label


def get_max_weighted_clusters(graph, node_name):
    maxval = 0
    maxclustids = []
    cdict = {}
    for n, nbrs in graph.graf.adjacency_iter():
        if n == node_name:
            for nbr, eattr in nbrs.iteritems():
                weight = eattr['weight']
                #print graph.graf.node[nbr]
                cl = graph.graf.node[nbr]['CLID']
                if cdict.__contains__(cl):
                    cdict[cl] += weight
                else:
                    cdict[cl] = weight
    for cl, weight in cdict.iteritems():
        if maxval < weight:
            maxval = weight
            maxclustids = [cl]
        elif maxval == weight:
            maxclustids.append(cl)
    clusterlist = []
    for clust in clusterglobals.clusters_list:
        if clust.label in maxclustids:
            clusterlist.append(clusterglobals.get_cluster(clust.label))
    #return maxclustids
    return clusterlist


def create_weighted_edges_list(node_data_dict):
    weighted_nodes_li = []
    for node_name, node_data in node_data_dict.iteritems():
        for nbr, weight in node_data:
            weighted_nodes_li.append(tuple([node_name, nbr, weight]))
    return weighted_nodes_li

def random_classification(graph):
    for node in graph.graf.nodes():
        clusters_li = get_max_weighted_clusters(graph, node)
        best_cluster = random_cluster(clusters_li)
        if best_cluster:
            old_cluster_id = graph.graf.node[node]['CLID']
            tags = graph.graf.node[node]['tags']
            old_cluster = get_cluster(old_cluster_id)
            st = old_cluster.remove_node(graph, node)
            if st == None:
                replace_cluster(old_cluster)
            else:
                replace_cluster(old_cluster, remove = True)
            best_cluster.add_node(node, tags)
            replace_cluster(best_cluster)
            change_node_cluster(graph, node, best_cluster.label)
        else:
            pass
        #clusterglobals.print_clusters()

def calculated_clustering(graph):
    pass
