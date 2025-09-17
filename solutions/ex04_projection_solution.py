from typing import Dict, Set
from hypergraphx.core.hypergraph import Hypergraph
from collections import defaultdict

def clique_projection_neighbors(hg: Hypergraph) -> Dict[str, Set[str]]:
    nbrs: Dict[str, Set[str]] = defaultdict(set)
    # Ensure all nodes appear as keys
    for u in hg.get_nodes():
        nbrs[str(u)]  # touch

    # For each node, every other member in an incident edge is a neighbor
    for u in hg.get_nodes():
        u = str(u)
        for e in hg.get_incident_edges(u):
            members = list(map(str, e))
            for v in members:
                if v != u:
                    nbrs[u].add(v)
                    nbrs[v].add(u)  # symmetry
    return {u: set(vs) for u, vs in nbrs.items()}

def clique_projection_degree(hg: Hypergraph) -> Dict[str, int]:
    nbrs = clique_projection_neighbors(hg)
    return {u: len(vs) for u, vs in nbrs.items()}
