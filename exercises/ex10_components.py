"""
Exercise 10 — Connected components

Implement:
- components(hg) -> List[List[str]]
- largest_component_size(hg) -> int

Notes:
- Use HGX: hg.connected_components(), hg.largest_component_size()
- Return component node lists sorted (as strings). 
"""

from typing import List
from hypergraphx.core.hypergraph import Hypergraph

def components(hg: Hypergraph) -> List[List[str]]:
    """
    Return connected components as sorted lists of strings.
    """
    # TODO: implement using HGX built-ins (e.g., hg.connected_components()).
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def largest_component_size(hg: Hypergraph) -> int:
    """
    Return size (in nodes) of the largest component.
    """
    # TODO: implement using HGX built-ins (e.g., hg.largest_component_size()).
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
