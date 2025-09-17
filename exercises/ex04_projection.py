"""
Exercise 4 — Simple 2-clique projection (neighbors & degrees)

Goal
----
Compute the pairwise (2-clique) projection:
- Two nodes are adjacent if they co-occur in at least one hyperedge.

Implement:
- clique_projection_neighbors(hg) -> dict {node: set(neighbors)}
- clique_projection_degree(hg)    -> dict {node: int}  (size of its neighbor set)

Hints
-----
- For each node u, iterate over hg.get_incident_edges(u).
- For each such edge, add all other members of the edge as neighbors of u.
- Keep neighbors symmetric (if v is in N[u], ensure u is in N[v]).
"""

from typing import Dict, Set
from hypergraphx.core.hypergraph import Hypergraph

def clique_projection_neighbors(hg: Hypergraph) -> Dict[str, Set[str]]:
    """
    Return a dict mapping node -> set of neighbors in the 2-clique projection.
    """
    # TODO: build neighbor sets using incident edges.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def clique_projection_degree(hg: Hypergraph) -> Dict[str, int]:
    """
    Return a dict node -> projection degree (len of its neighbor set).
    """
    # TODO: compute degrees from clique_projection_neighbors(hg).
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
