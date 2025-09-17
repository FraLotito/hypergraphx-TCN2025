"""
Exercise 12 — Degree-rank sensitivity to adding a hyperedge

Implement:
- degree_rank(hg) -> dict {node -> rank} (1 = highest degree; ties broken lexicographically)
- add_edge_and_rank_changes(hg, new_edge, top=3) -> list of top 'top' nodes with largest absolute rank change
  (Return node labels; tie-break by lexicographic order.)
"""

from typing import Dict, Iterable, List
from hypergraphx.core.hypergraph import Hypergraph

def degree_rank(hg: Hypergraph) -> Dict[str, int]:
    # TODO: compute ranks from degrees with lexicographic tie-breaking.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def add_edge_and_rank_changes(hg: Hypergraph, new_edge: Iterable[str], top: int = 3) -> List[str]:
    # TODO: add the edge (on a copy), recompute ranks, return top movers by |Δrank|.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
