"""
Exercise 1 — Hyperedge sizes & node degrees (HGX Core)

Implement:
- edge_size_distribution(hg) -> dict {size: count}
- node_degrees(hg)          -> dict {node: hyperdegree}
- top_k_by_degree(hg, k)    -> list of node IDs sorted by (deg desc, id asc)
"""

from typing import Dict, List
from hypergraphx.core.hypergraph import Hypergraph

def edge_size_distribution(hg: Hypergraph) -> Dict[int, int]:
    """
    Use HGX's distribution_sizes() (or equivalent) and return a plain dict.
    """
    # TODO: compute and return the size distribution.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def node_degrees(hg: Hypergraph) -> Dict[str, int]:
    """
    Iterate over hg.get_nodes() and use hg.degree(u).
    """
    # TODO: compute {node: degree}.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def top_k_by_degree(hg: Hypergraph, k: int) -> List[str]:
    """
    Rank nodes by (-degree, node_id) and return exactly k node IDs.
    """
    # TODO: produce the top-k ranking.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
