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

def test_participation_and_entropy():
    mod = load("ex11_participation_entropy")
    hg = _toy()

    part = mod.participation_by_size(hg)
    exp_A = {3: 2, 2: 1}
    assert part.get("A") == exp_A, (
        f"Wrong participation-by-size for 'A'. Expected {exp_A}, got {part.get('A')}."
    )
    exp_F = {3: 1}
    assert part.get("F") == exp_F, (
        f"Wrong participation-by-size for 'F'. Expected {exp_F}, got {part.get('F')}."
    )

    ent = mod.participation_entropy(hg)
    expected_A = 0.6365141682948128  # -(2/3 ln(2/3) + 1/3 ln(1/3))
    assert abs(ent.get("A", -1) - expected_A) < 1e-9, (
        f"Entropy for 'A' incorrect. Expected ~{expected_A}, got {ent.get('A')}."
    )
    assert abs(ent.get("F", -1) - 0.0) < 1e-12, (
        f"Entropy for 'F' should be 0.0, got {ent.get('F')}."
    )
