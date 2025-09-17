"""
Exercise 08 — Top-K hyperedge overlaps (Jaccard)

Implement:
- topk_edge_jaccard(hg, k) -> list of tuples: [(edge_key1, edge_key2, jaccard), ...]
  where each edge_key is a sorted tuple of node labels and the list is sorted by:
  (jaccard DESC, edge_key1 ASC, edge_key2 ASC). Always ensure edge_key1 < edge_key2.
"""

from typing import List, Tuple
from hypergraphx.core.hypergraph import Hypergraph

EdgeKey = Tuple[str, ...]

def topk_edge_jaccard(hg: Hypergraph, k: int) -> List[Tuple[EdgeKey, EdgeKey, float]]:
    # TODO: compute all pairwise Jaccard scores and return top-k as specified.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
