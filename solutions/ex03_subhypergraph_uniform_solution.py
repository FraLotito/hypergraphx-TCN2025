from hypergraphx.core.hypergraph import Hypergraph

def sub_of_size(hg: Hypergraph, size: int) -> Hypergraph:
    return hg.subhypergraph_by_orders(sizes=[size])

def is_uniform(hg: Hypergraph) -> bool:
    return hg.is_uniform()
