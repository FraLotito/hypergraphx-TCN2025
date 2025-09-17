"""
Exercise 11 — Participation by edge size & entropy

Implement:
- participation_by_size(hg) -> dict {node -> dict {size -> count of incident edges of that size}}
- participation_entropy(hg) -> dict {node -> Shannon entropy (natural log) of that size distribution}
  (Define H = 0.0 when degree(node) = 0.)
"""

from typing import Dict
from hypergraphx.core.hypergraph import Hypergraph

def participation_by_size(hg: Hypergraph) -> Dict[str, Dict[int, int]]:
    # TODO: build per-node histograms of incident edge sizes.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def participation_entropy(hg: Hypergraph) -> Dict[str, float]:
    # TODO: compute -Σ_s p_s log(p_s) per node (natural log).
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
