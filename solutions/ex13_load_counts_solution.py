from typing import Tuple
from hypergraphx.readwrite import load_hypergraph

def load_counts(path: str) -> Tuple[int, int]:
    hg = load_hypergraph(path)
    return int(hg.num_nodes()), int(hg.num_edges())
