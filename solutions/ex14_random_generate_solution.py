from typing import List, Optional, Dict
from hypergraphx.core.hypergraph import Hypergraph
from hypergraphx.generation.random import random_hypergraph

SIZES = [2, 3, 4, 5, 6]

def _edges_by_size_for_majority(total_min: int, target_size: int) -> Dict[int, int]:
    """
    Build a histogram with a strict majority for `target_size` and totals >= total_min.
    We use a small baseline for non-target sizes and assign the rest to the target.
    """
    non_target = [s for s in SIZES if s != target_size]
    baseline = 1 * len(non_target)  # 1 edge for each non-target size
    # ensure target strictly more than any other; allocate a cushion above the minimum
    target_count = max(total_min - baseline, 1) + 2  # +2 cushion
    total = target_count + baseline
    hist = {s: (1 if s in non_target else target_count) for s in SIZES}
    # If we want to slightly exceed total_min to be robust to any generator de-duplication,
    # this histogram intentionally produces >= total_min edges.
    return hist

def generate_five_majority(n_min: int = 10, e_min: int = 10, seed: Optional[int] = None) -> List[Hypergraph]:
    hgs: List[Hypergraph] = []
    # Keep nodes exactly n_min (spec allows >=; tests only require >=)
    n = n_min
    for idx, target in enumerate(SIZES):
        edges_by_size = _edges_by_size_for_majority(e_min, target)
        sd = None if seed is None else seed + idx
        hg = random_hypergraph(num_nodes=n, num_edges_by_size=edges_by_size, seed=sd)
        hgs.append(hg)
    return hgs
