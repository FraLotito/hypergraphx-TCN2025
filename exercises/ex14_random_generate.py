"""
Exercise 14 — Five seeded random hypergraphs with different majority edge sizes

Implement:
- generate_five_majority(n_min=10, e_min=10, seed=None) -> list[Hypergraph]

Requirements
------------
- Use HGX: from hypergraphx.generation.random import random_hypergraph
- Return exactly 5 hypergraphs.
- For i in [0..4], hypergraph i must have a STRICT MAJORITY of its hyperedges
  of size S_i, where S = [2, 3, 4, 5, 6].
- Each hypergraph must have at least n_min nodes and at least e_min hyperedges.
- Make the result reproducible with `seed` (e.g., derive seeds as seed+i).

Starter
-------
Keep the NotImplementedError until you implement the function.
"""

from typing import List, Optional
from hypergraphx.core.hypergraph import Hypergraph

def generate_five_majority(n_min: int = 10, e_min: int = 10, seed: Optional[int] = None) -> List[Hypergraph]:
    """
    Return [HG_size2_majority, HG_size3_majority, HG_size4_majority, HG_size5_majority, HG_size6_majority].

    Each element must have:
      - >= n_min nodes and >= e_min hyperedges
      - a strict majority of edges of its designated size (2..6).
    """
    # TODO: call random_hypergraph(num_nodes=..., num_edges_by_size=..., seed=...).
    # Hint: give non-target sizes a small baseline count and put the rest on the target size.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
