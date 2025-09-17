"""
Exercise 05 — Edge size buckets & node coverage

Implement:
- edge_size_buckets(hg) -> dict {size: count}
- nodes_covered_by_size(hg) -> dict {size: set(nodes)}
- coverage_share_by_size(hg) -> dict {size: float in [0,1]}
- cumulative_coverage_share(hg, ascending=True) -> dict {size: cumulative share}
"""

from typing import Dict, Set
from hypergraphx.core.hypergraph import Hypergraph

def edge_size_buckets(hg: Hypergraph) -> Dict[int, int]:
    """
    Return a plain dict mapping hyperedge size -> how many edges have that size.
    """
    # TODO: compute from hg.distribution_sizes() or by iterating hg.get_edges()
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def nodes_covered_by_size(hg: Hypergraph) -> Dict[int, Set[str]]:
    """
    Return a dict mapping size -> set of nodes that appear in any edge of that size.
    """
    # TODO: build size->nodes set
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def coverage_share_by_size(hg: Hypergraph) -> Dict[int, float]:
    """
    For each size s, share = (# unique nodes in size-s edges) / hg.num_nodes().
    """
    # TODO: compute shares using nodes_covered_by_size()
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def cumulative_coverage_share(hg: Hypergraph, ascending: bool = True) -> Dict[int, float]:
    """
    Cumulative union of covered nodes as sizes progress (ascending or descending order).
    Return dict {size: share} for sizes in the order they are accumulated.
    """
    # TODO: accumulate node coverage over sorted sizes
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
