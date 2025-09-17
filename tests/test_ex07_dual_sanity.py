from tests.helpers import load
from hypergraphx.core.hypergraph import Hypergraph

def _toy():
    hg = Hypergraph()
    hg.add_nodes(list("ABCDEFGH"))
    hg.add_edges([
        ("A","B","C"), ("B","C","D"), ("A","D"), ("E","F","G"), ("A","E","H")
    ])
    return hg

def test_dual_sanity_properties():
    mod = load("ex07_dual_sanity")
    hg = _toy()

    dnodes = mod.dual_nodes(hg)
    assert len(dnodes) == hg.num_edges(), (
        f"Dual 'node' count should equal #original edges ({hg.num_edges()}), got {len(dnodes)}."
    )

    ddeg = mod.dual_degrees(hg)
    for ek, val in ddeg.items():
        assert val == len(ek), (
            f"Dual degree for edge-key {ek} should equal its size {len(ek)}, got {val}."
        )

    dinc = mod.dual_incidence(hg)
    for u in map(str, hg.get_nodes()):
        expected = hg.degree(u)
        got = len(dinc.get(u, set()))
        assert got == expected, (
            f"Dual incidence mismatch for node '{u}'. Expected {expected} incident dual-nodes, got {got}."
        )
