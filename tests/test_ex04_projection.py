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

def test_projection_neighbors_and_degrees():
    mod = load("ex04_projection")
    hg = _make_hg()

    expected_nbrs = {
        "A": {"B","C","D","E","H"},
        "B": {"A","C","D"},
        "C": {"A","B","D"},
        "D": {"A","B","C"},
        "E": {"A","F","G","H"},
        "F": {"E","G"},
        "G": {"E","F"},
        "H": {"A","E"},
    }

    nbrs = mod.clique_projection_neighbors(hg)

    # Check node coverage first
    expected_keys, got_keys = set(expected_nbrs.keys()), set(nbrs.keys())
    missing = expected_keys - got_keys
    extra   = got_keys - expected_keys
    assert not missing and not extra, (
        "Neighbor dictionary has the wrong set of nodes. "
        f"Missing keys: {sorted(missing)} | Extra keys: {sorted(extra)}"
    )

    # Check per-node neighbor sets
    for u in sorted(expected_nbrs.keys()):
        exp, got = set(expected_nbrs[u]), set(nbrs[u])
        assert got == exp, (
            f"Wrong neighbors for node '{u}'. Expected {sorted(exp)}, got {sorted(got)}."
        )

    # Degrees
    expected_deg = {u: len(v) for u, v in expected_nbrs.items()}
    deg = mod.clique_projection_degree(hg)

    # Same key coverage check
    expk, gotk = set(expected_deg.keys()), set(deg.keys())
    missing_k, extra_k = expk - gotk, gotk - expk
    assert not missing_k and not extra_k, (
        "Projection degree dict has wrong keys. "
        f"Missing: {sorted(missing_k)} | Extra: {sorted(extra_k)}"
    )

    # Per-node degree check
    mismatches = {u: (deg.get(u), expected_deg[u]) for u in expected_deg if deg.get(u) != expected_deg[u]}
    assert not mismatches, (
        "Wrong projection degrees for some nodes. "
        f"Mismatches (got, expected): {mismatches}"
    )
