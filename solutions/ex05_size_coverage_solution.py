from typing import Dict, Set
from hypergraphx.core.hypergraph import Hypergraph

def edge_size_buckets(hg: Hypergraph) -> Dict[int, int]:
    return dict(sorted(hg.distribution_sizes().items()))

def nodes_covered_by_size(hg: Hypergraph) -> Dict[int, Set[str]]:
    out: Dict[int, Set[str]] = {}
    for e in hg.get_edges():
        s = len(e)
        out.setdefault(s, set()).update(map(str, e))
    return {k: set(sorted(v)) for k, v in sorted(out.items())}

def coverage_share_by_size(hg: Hypergraph) -> Dict[int, float]:
    total = float(hg.num_nodes()) if hg.num_nodes() else 1.0
    covered = nodes_covered_by_size(hg)
    return {s: len(v)/total for s, v in covered.items()}

def cumulative_coverage_share(hg: Hypergraph, ascending: bool = True) -> Dict[int, float]:
    sizes = sorted(edge_size_buckets(hg).keys(), reverse=not ascending)
    total = float(hg.num_nodes()) if hg.num_nodes() else 1.0
    seen: Set[str] = set()
    out: Dict[int, float] = {}
    by_size = nodes_covered_by_size(hg)
    for s in sizes:
        seen |= by_size.get(s, set())
        out[s] = len(seen)/total
    return out
