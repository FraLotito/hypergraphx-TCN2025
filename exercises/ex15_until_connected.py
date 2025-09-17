"""
Exercise 15 — Add random edges (size 2–4) until the hypergraph is connected (seeded)

Implement:
- grow_until_connected(n=20, seed=None) -> (Hypergraph, int)
  Return (hg, total_edges_added), where:
    • hg has exactly n nodes (strings "0"..)
    • you add UNIQUE random hyperedges
    • each edge size is chosen uniformly at random from {2,3,4}
    • pick edge members uniformly without replacement
    • stop when hg is connected (use HGX built-ins)

Notes:
- Use the 'seed' to make runs reproducible.
- Keep the NotImplementedError until you implement the function.
"""

from typing import Optional, Tuple
from hypergraphx.core.hypergraph import Hypergraph

def grow_until_connected(n: int = 20, seed: Optional[int] = None) -> Tuple[Hypergraph, int]:
    """
    Return (hypergraph, num_edges_added).
    """
    # TODO: seeded loop; add unique edges of size in {2,3,4}; stop when connected.
    # Hints: use hg.largest_component_size() or hg.connected_components()
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
