from tests.helpers import load
from hypergraphx.core.hypergraph import Hypergraph

def _toy():
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

def test_rank_changes_after_adding_edge():
    mod = load("ex12_rank_change")
    hg = _toy()

    new_edge = ("E","F","G","H")  # boosts E from degree 2 -> 3
    top3 = mod.add_edge_and_rank_changes(hg, new_edge, top=3)

    expected = ["E","B","C"]  # E jumps most; B and C shift by 1 (tie-break lexicographically)
    assert top3 == expected, (
        f"Top rank changes incorrect. Expected {expected}, got {top3}. "
        "Remember: rank 1 is best; break ties lexicographically."
    )
