from typing import Set, Tuple, List
from hypergraphx.core.hypergraph import Hypergraph

EdgeKey = Tuple[str, ...]

def _ek(e) -> EdgeKey:
    return tuple(sorted(map(str, e)))

def filter_edges_by_min_overlap(hg: Hypergraph, tau: int) -> Hypergraph:
    edges: List[Set[str]] = [set(map(str, e)) for e in hg.get_edges()]
    keep = [False]*len(edges)
    for i, Ei in enumerate(edges):
        best = 0
        for j, Ej in enumerate(edges):
            if i == j: continue
            best = max(best, len(Ei & Ej))
            if best >= tau:
                keep[i] = True
                break
    new_hg = Hypergraph()
    # Add only nodes that appear in kept edges
    kept_edges = [tuple(sorted(e)) for i, e in enumerate(edges) if keep[i]]
    if kept_edges:
        node_set = sorted(set().union(*kept_edges))
        new_hg.add_nodes(node_set)
        new_hg.add_edges(kept_edges)
    return new_hg

def remaining_edge_keys(hg: Hypergraph) -> Set[EdgeKey]:
    return { _ek(e) for e in hg.get_edges() }
