from typing import Dict, List
from hypergraphx.core.hypergraph import Hypergraph

def edge_size_distribution(hg: Hypergraph) -> Dict[int, int]:
    # HGX returns a Counter-like mapping; normalize to plain dict (sorted for determinism).
    return dict(sorted(hg.distribution_sizes().items()))

def node_degrees(hg: Hypergraph) -> Dict[str, int]:
    return {str(u): hg.degree(u) for u in hg.get_nodes()}

def top_k_by_degree(hg: Hypergraph, k: int) -> List[str]:
    deg = node_degrees(hg)
    return [u for u, _ in sorted(deg.items(), key=lambda x: (-x[1], x[0]))[:k]]
