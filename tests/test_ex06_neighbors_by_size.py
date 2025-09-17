from tests.helpers import load
from hypergraphx.core.hypergraph import Hypergraph

def _toy():
    hg = Hypergraph()
    hg.add_nodes(list("ABCDEFGH"))
    hg.add_edges([
        ("A","B","C"), ("B","C","D"), ("A","D"), ("E","F","G"), ("A","E","H")
    ])
    return hg

def test_neighbors_by_size():
    mod = load("ex06_neighbors_by_size")
    hg = _toy()

    got3 = mod.neighbors_by_size(hg, "A", 3)
    exp3 = {"B","C","E","H"}
    assert got3 == exp3, (
        f"Neighbors of 'A' via size-3 edges incorrect. Expected {sorted(exp3)}, got {sorted(got3)}."
    )

    got2 = mod.neighbors_by_size(hg, "A", 2)
    exp2 = {"D"}
    assert got2 == exp2, (
        f"Neighbors of 'A' via size-2 edges incorrect. Expected {sorted(exp2)}, got {sorted(got2)}."
    )
