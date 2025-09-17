"""
Exercise 13 — Load dataset & report counts (HGX `load_hypergraph`)

Implement:
- load_counts(path) -> tuple[int, int]   # (num_nodes, num_edges)

Notes:
- Accept ONLY a file path under data/ (e.g., "data/contacts-high-school.json").
- Return values (do not print).
"""

from typing import Tuple

def load_counts(path: str) -> Tuple[int, int]:
    """
    Return (num_nodes, num_edges) for the dataset at `path`.
    """
    # TODO: use hypergraphx.io.load_hypergraph(path) then hg.num_nodes(), hg.num_edges()
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
