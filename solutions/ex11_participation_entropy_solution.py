from typing import Dict
from math import log
from collections import defaultdict
from hypergraphx.core.hypergraph import Hypergraph

def participation_by_size(hg: Hypergraph) -> Dict[str, Dict[int, int]]:
    out: Dict[str, Dict[int, int]] = defaultdict(lambda: defaultdict(int))
    for e in hg.get_edges():
        s = len(e)
        for u in map(str, e):
            out[u][s] += 1
    # Normalize to plain dicts (sorted for determinism)
    return {u: {k: v for k, v in sorted(sz.items())} for u, sz in sorted(out.items())}

def participation_entropy(hg: Hypergraph) -> Dict[str, float]:
    part = participation_by_size(hg)
    ent: Dict[str, float] = {}
    for u, hist in part.items():
        total = sum(hist.values())
        if total == 0:
            ent[u] = 0.0
            continue
        H = 0.0
        for c in hist.values():
            p = c / total
            H -= p * log(p)
        ent[u] = H
    return ent
