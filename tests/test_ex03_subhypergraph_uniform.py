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

def test_sub_of_size_and_uniform():
    mod = load("ex03_subhypergraph_uniform")
    hg = _make_hg()

    hg3 = mod.sub_of_size(hg, 3)
    assert hg3.num_edges() == 4, (
        f"Restricting to size-3 edges should yield 4 edges, got {hg3.num_edges()}."
    )
    assert hg3.num_nodes() == 8, (
        f"After restricting to size-3 edges, expected 8 nodes, got {hg3.num_nodes()}."
    )

    uniform = mod.is_uniform(hg3)
    assert uniform is True, (
        "Subhypergraph of size-3 edges should be uniform (all edges size 3), "
        f"but is_uniform returned {uniform}."
    )
