from tests.helpers import load
from hypergraphx.core.hypergraph import Hypergraph

def _toy():
    hg = Hypergraph()
    hg.add_nodes(list("ABCDEFGH"))
    hg.add_edges([
        ("A","B","C"), ("B","C","D"), ("A","D"), ("E","F","G"), ("A","E","H")
    ])
    return hg

def test_topk_edge_jaccard():
    mod = load("ex08_edge_overlap")
    hg = _toy()

    got = mod.topk_edge_jaccard(hg, k=3)

    # Expected (edge_key1, edge_key2, jaccard)
    exp = [
        (("A","B","C"), ("B","C","D"), 0.5),
        (("A","B","C"), ("A","D"), 0.25),
        (("A","D"), ("A","E","H"), 0.25),
    ]

    # Shape and ordering checks with informative errors
    assert len(got) == len(exp), (
        f"Expected {len(exp)} top pairs, got {len(got)}: {got}."
    )
    for (g1, g2, gj), (e1, e2, ej) in zip(got, exp):
        assert g1 == e1 and g2 == e2, (
            f"Wrong pair order or keys. Expected {(e1, e2)}, got {(g1, g2)}."
        )
        assert abs(gj - ej) < 1e-9, (
            f"Wrong Jaccard for pair {(e1, e2)}. Expected {ej}, got {gj}."
        )
