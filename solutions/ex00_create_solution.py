from hypergraphx.core.hypergraph import Hypergraph

def build_hypergraph_hgx() -> Hypergraph:
    hg = Hypergraph()
    # 8 nodes
    hg.add_nodes(list("ABCDEFGH"))
    # 5 hyperedges (mixed sizes, overlapping allowed)
    hg.add_edges([
        ("A","B","C"),
        ("B","C","D"),
        ("A","D"),
        ("E","F","G"),
        ("A","E","H"),
    ])
    return hg
