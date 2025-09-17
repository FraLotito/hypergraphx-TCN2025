from typing import List
from hypergraphx.core.hypergraph import Hypergraph

def components(hg: Hypergraph) -> List[List[str]]:
    """
    Return connected components as sorted lists of node labels (strings),
    using HGX's built-in connected components.
    """
    comps = hg.connected_components()  # HGX API
    return sorted([sorted(map(str, comp)) for comp in comps])

def largest_component_size(hg: Hypergraph) -> int:
    """
    Return the size (in nodes) of the largest connected component,
    using HGX's built-in method.
    """
    return int(hg.largest_component_size())  # HGX API
