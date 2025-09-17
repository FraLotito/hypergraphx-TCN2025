from typing import Optional, Tuple, Set
from hypergraphx.core.hypergraph import Hypergraph
import random

def _is_connected(hg: Hypergraph) -> bool:
    try:
        return int(hg.largest_component_size()) == hg.num_nodes()
    except AttributeError:
        comps = hg.connected_components()
        return max((len(c) for c in comps), default=0) == hg.num_nodes()

def grow_until_connected(n: int = 20, seed: Optional[int] = None) -> Tuple[Hypergraph, int]:
    rng = random.Random(seed)

    hg = Hypergraph()
    nodes = [str(i) for i in range(n)]
    hg.add_nodes(nodes)

    seen: Set[frozenset] = set()  # frozensets of node labels

    while not _is_connected(hg):
        s = rng.randint(2, 4)          # edge size ∈ {2,3,4}
        members = tuple(sorted(rng.sample(nodes, s)))  # sample without replacement
        key = frozenset(members)
        if key in seen:
            continue
        seen.add(key)
        hg.add_edges([members])

        # (Optional) safety: avoid pathological loops
        if len(seen) > 50_000 and not _is_connected(hg):
            break

    return hg, hg.num_edges()
