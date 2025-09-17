# solutions/ex12_rank_change_solution.py
from typing import Dict, Iterable, List
from hypergraphx.core.hypergraph import Hypergraph

def _degree_map(hg: Hypergraph) -> Dict[str, int]:
    return {str(u): hg.degree(u) for u in hg.get_nodes()}

def _rank_from_degrees(deg: Dict[str, int]) -> Dict[str, int]:
    order = sorted(deg.items(), key=lambda x: (-x[1], x[0]))  # degree desc, id asc
    return {u: i + 1 for i, (u, _) in enumerate(order)}

def degree_rank(hg: Hypergraph) -> Dict[str, int]:
    return _rank_from_degrees(_degree_map(hg))

def add_edge_and_rank_changes(hg: Hypergraph, new_edge: Iterable[str], top: int = 3) -> List[str]:
    # Degrees before
    deg0 = _degree_map(hg)

    # Degrees after: +1 for each unique node in the new edge (including new nodes)
    deg1 = deg0.copy()
    for u in set(map(str, new_edge)):    # dedupe just in case
        deg1[u] = deg1.get(u, 0) + 1

    # Ranks before/after
    r0 = _rank_from_degrees(deg0)
    r1 = _rank_from_degrees(deg1)

    # Compare on the union of nodes (so brand-new nodes are included)
    universe = sorted(set(deg1) | set(r0))
    diffs = [(u, abs(r0.get(u, len(universe)) - r1.get(u, len(universe)))) for u in universe]
    diffs.sort(key=lambda x: (-x[1], x[0]))  # biggest change first, tie-break by id

    return [u for u, _ in diffs[:top]]
