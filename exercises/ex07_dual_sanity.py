"""
Exercise 07 — Dual hypergraph sanity (edges ↔ nodes)

Implement:
- dual_nodes(hg) -> set of edge-keys (each edge-key = sorted tuple of node labels)
- dual_incidence(hg) -> dict {original_node -> set of dual nodes (edge-keys) it belongs to}
- dual_degrees(hg) -> dict {edge-key -> int} (size of the original edge)

Sanity properties (the tests will check):
- len(dual_nodes) == hg.num_edges()
- dual_degrees[edge_key] == len(edge_key)
- For every original node u: len(dual_incidence[u]) == hg.degree(u)
"""

from typing import Dict, Set, Tuple
from hypergraphx.core.hypergraph import Hypergraph

EdgeKey = Tuple[str, ...]
Incidence = Dict[str, Set[EdgeKey]]

def dual_nodes(hg: Hypergraph) -> Set[EdgeKey]:
    # TODO: collect sorted tuples from hg.get_edges()
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def dual_incidence(hg: Hypergraph) -> Incidence:
    # TODO: map each original node -> set of edge-keys it is incident to
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def dual_degrees(hg: Hypergraph) -> Dict[EdgeKey, int]:
    # TODO: map each edge-key -> its size (len of the tuple)
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
