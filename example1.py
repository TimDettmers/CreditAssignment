import operator
import networkx as nx
import numpy as np

G = nx.DiGraph()

# population
G.add_edge('world', 'world', weight=10**10)

# fraction of ideas
G.add_edge('world', 'P1', weight=1.0)
# fraction of people influenced
G.add_edge('P1', 'world', weight=1.0/(10**10))
# direct connections to influenced peoples
G.add_edge('P1', 'P2', weight=1.0)

# fraction of people influenced
G.add_edge('P2', 'world', weight=1.0/(10**10))
# fraction of ideas from P1 which were understood
G.add_edge('P2', 'P1', weight=1.0)
# direct connections to influenced peoples
G.add_edge('P3', 'P2', weight=1.0)

# fraction of people influenced
G.add_edge('P3', 'world', weight=1.0)
# fraction of ideas from P2 which were understood
G.add_edge('P2', 'P3', weight=1.0)

results = nx.pagerank(G)

total_contributions = 0
for key, value in results.items():
    if key != 'world': total_contributions += value


sorted_by_contribution = sorted(results.items(), key=operator.itemgetter(1), reverse=True)
for key, value in sorted_by_contribution:
    if key == 'world': continue
    print('Name: {0}\t PageRank: {1}\t Relative contribution: {2}'.format(key, np.round(value,4), np.round(value/total_contributions, 4)))

