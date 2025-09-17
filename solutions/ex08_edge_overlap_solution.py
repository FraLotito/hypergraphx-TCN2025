from typing import List, Tuple
from hypergraphx.core.hypergraph import Hypergraph
from itertools import combinations

EdgeKey = Tuple[str, ...]

def _ek(e) -> EdgeKey:
    return tuple(sorted(map(str, e)))

def _jaccard(a: set, b: set) -> float:
    u = len(a|b)
    return (len(a&b)/u) if u else 0.0

def topk_edge_jaccard(hg: Hypergraph, k: int) -> List[Tuple[EdgeKey, EdgeKey, float]]:
    edges = [set(map(str, e)) for e in hg.get_edges()]
    keys  = [_ek(e) for e in hg.get_edges()]
    triples: List[Tuple[EdgeKey, EdgeKey, float]] = []
    for (i, j) in combinations(range(len(edges)), 2):
        e1, e2 = keys[i], keys[j]
        if e2 < e1:  # enforce e1 < e2
            e1, e2 = e2, e1
            a, b = edges[j], edges[i]
        else:
            a, b = edges[i], edges[j]
        triples.append((e1, e2, _jaccard(a, b)))
    triples.sort(key=lambda t: (-t[2], t[0], t[1]))
    return triples[:k]
