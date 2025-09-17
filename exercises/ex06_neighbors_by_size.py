"""
Exercise 06 — Neighbors filtered by exact hyperedge size

Implement:
- neighbors_by_size(hg, node, s) -> set of neighbors that co-occur with `node` in edges of size exactly s.
"""

from typing import Set
from hypergraphx.core.hypergraph import Hypergraph

def neighbors_by_size(hg: Hypergraph, node: str, size: int) -> Set[str]:
    """
    Use hg.get_neighbors(node, size=size).
    """
    # TODO: return neighbors as a set of node labels (strings)
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
