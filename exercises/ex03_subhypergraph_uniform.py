"""
Exercise 3 — Uniform subhypergraphs

Implement:
- sub_of_size(hg, size) -> subhypergraph containing only edges of that size
- is_uniform(hg)        -> True iff all edges have the same size
"""

from hypergraphx.core.hypergraph import Hypergraph

def sub_of_size(hg: Hypergraph, size: int) -> Hypergraph:
    """
    Use hg.subhypergraph_by_orders(sizes=[size]).
    """
    # TODO: return the subhypergraph restricted to edges of the given size.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")

def is_uniform(hg: Hypergraph) -> bool:
    """
    Use hg.is_uniform().
    """
    # TODO: return True/False depending on uniformity.
    # Remove the line below when you start implementing.
    raise NotImplementedError("Implement me!")
