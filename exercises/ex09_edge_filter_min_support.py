"""
Exercise 09 — Filter edges by min shared-node overlap (tau)

Implement:
- filter_edges_by_min_overlap(hg, tau) -> new Hypergraph containing only edges E
  such that max_{F != E} |E ∩ F| >= tau.
- remaining_edge_keys(hg) -> set of edge-keys (sorted tuples) in the given hypergraph.
"""

from typing import Set, Tuple
from hypergraphx.core.hypergraph import Hypergraph

EdgeKey = Tuple[str, ...]

def filter_edges_by_min_overlap(hg: Hypergraph, tau: int) -> Hypergraph:
    # TODO: construct and return a filtered hypergraph
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def remaining_edge_keys(hg: Hypergraph) -> Set[EdgeKey]:
    # TODO: return set of sorted tuples representing edges of hg
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
