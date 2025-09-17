from typing import List, Set, Tuple
from hypergraphx.core.hypergraph import Hypergraph

def incident_edges(hg: Hypergraph, node: str) -> List[Tuple[str, ...]]:
    # Convert each incident edge to a sorted tuple; return a globally sorted list.
    edges = [tuple(sorted(map(str, e))) for e in hg.get_incident_edges(node)]
    return sorted(edges)

def neighbors_by_size(hg: Hypergraph, node: str, size: int) -> Set[str]:
    return set(map(str, hg.get_neighbors(node, size=size)))

def largest_component_size(hg: Hypergraph) -> int:
    return hg.largest_component_size()
