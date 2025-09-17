from typing import Dict, Set, Tuple
from hypergraphx.core.hypergraph import Hypergraph
from collections import defaultdict

EdgeKey = Tuple[str, ...]
Incidence = Dict[str, Set[EdgeKey]]

def _edge_key(e) -> EdgeKey:
    return tuple(sorted(map(str, e)))

def dual_nodes(hg: Hypergraph) -> Set[EdgeKey]:
    return { _edge_key(e) for e in hg.get_edges() }

def dual_incidence(hg: Hypergraph) -> Incidence:
    inc: Incidence = defaultdict(set)
    for e in hg.get_edges():
        ek = _edge_key(e)
        for u in map(str, e):
            inc[u].add(ek)
    return {u: set(sorted(v)) for u, v in sorted(inc.items())}

def dual_degrees(hg: Hypergraph) -> Dict[EdgeKey, int]:
    return { _edge_key(e): len(e) for e in hg.get_edges() }
