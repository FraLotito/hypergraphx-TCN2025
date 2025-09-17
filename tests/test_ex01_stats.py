from tests.helpers import load
from hypergraphx.core.hypergraph import Hypergraph

def _make_hg():
    hg = Hypergraph()
    hg.add_nodes(list("ABCDEFGH"))
    hg.add_edges([
        ("A","B","C"),
        ("B","C","D"),
        ("A","D"),
        ("E","F","G"),
        ("A","E","H"),
    ])
    return hg

def test_edge_size_distribution_and_degrees_and_topk():
    mod = load("ex01_stats")
    hg = _make_hg()

    expected_sizes = {2: 1, 3: 4}
    sizes = mod.edge_size_distribution(hg)
    assert sizes == expected_sizes, (
        f"Wrong edge size distribution. Expected {expected_sizes}, got {sizes}."
    )

    expected_deg = {"A":3,"B":2,"C":2,"D":2,"E":2,"F":1,"G":1,"H":1}
    deg = mod.node_degrees(hg)
    assert deg == expected_deg, (
        f"Wrong node degree mapping. Expected {expected_deg}, got {deg}."
    )

    expected_top3 = ["A","B","C"]
    top3 = mod.top_k_by_degree(hg, 3)
    assert top3 == expected_top3, (
        f"Wrong top-3 by degree. Expected {expected_top3}, got {top3}. "
        "Remember to break ties lexicographically by node id."
    )
