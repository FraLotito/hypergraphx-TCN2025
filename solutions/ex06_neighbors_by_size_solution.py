from typing import Set
from hypergraphx.core.hypergraph import Hypergraph

def neighbors_by_size(hg: Hypergraph, node: str, size: int) -> Set[str]:
    return set(map(str, hg.get_neighbors(node, size=size)))
