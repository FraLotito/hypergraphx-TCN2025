from tests.helpers import load
from hypergraphx.core.hypergraph import Hypergraph

def _toy():
    hg = Hypergraph()
    hg.add_nodes(list("ABCDEFGH"))
    hg.add_edges([
        ("A","B","C"), ("B","C","D"), ("A","D"), ("E","F","G"), ("A","E","H")
    ])
    return hg

def test_filter_tau_2_and_1():
    mod = load("ex09_edge_filter_min_support")
    hg = _toy()

    # tau = 2 keeps only edges sharing at least 2 nodes with some other edge
    f2 = mod.filter_edges_by_min_overlap(hg, tau=2)
    got2 = mod.remaining_edge_keys(f2)
    exp2 = {("A","B","C"), ("B","C","D")}
    assert got2 == exp2, (
        f"For tau=2 expected edges {sorted(exp2)}, got {sorted(got2)}."
    )
    assert f2.num_nodes() >= 4, (
        "Filtered hypergraph should have at least the nodes appearing in the remaining edges."
    )

    # tau = 1 keeps all edges in this toy example
    f1 = mod.filter_edges_by_min_overlap(hg, tau=1)
    got1 = mod.remaining_edge_keys(f1)
    exp1 = {("A","B","C"), ("B","C","D"), ("A","D"), ("E","F","G"), ("A","E","H")}
    assert got1 == exp1, (
        f"For tau=1 expected to keep all edges, but got {sorted(got1)}."
    )
