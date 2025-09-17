"""
Exercise 2 — Incident edges, neighbors-by-size, largest component

Implement:
- incident_edges(hg, node)        -> list of tuples, each tuple = sorted node labels of one incident edge; return list sorted
- neighbors_by_size(hg, node, s)  -> set of neighbors from edges with exact size s (use size=... argument)
- largest_component_size(hg)      -> int (size in nodes)
"""

from typing import List, Set, Tuple
from hypergraphx.core.hypergraph import Hypergraph

def incident_edges(hg: Hypergraph, node: str) -> List[Tuple[str, ...]]:
    """
    Use hg.get_incident_edges(node). Sort nodes within each edge, and sort the list.
    """
    # TODO: build and return the sorted list of incident edges.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def neighbors_by_size(hg: Hypergraph, node: str, size: int) -> Set[str]:
    """
    Use hg.get_neighbors(node, size=size) to filter by hyperedge size.
    """
    # TODO: return the neighbor set for the given size.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def largest_component_size(hg: Hypergraph) -> int:
    """
    Use hg.largest_component_size().
    """
    # TODO: return the size of the largest component.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
