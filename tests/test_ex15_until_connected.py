from tests.helpers import load
from hypergraphx.core.hypergraph import Hypergraph

def _edge_set(hg: Hypergraph):
    return {frozenset(map(str, e)) for e in hg.get_edges()}

def _sizes(hg: Hypergraph):
    return [len(e) for e in hg.get_edges()]

def _largest_component_size(hg: Hypergraph) -> int:
    try:
        return int(hg.largest_component_size())
    except AttributeError:
        comps = hg.connected_components()
        return max((len(c) for c in comps), default=0)

def test_grow_until_connected_seeded_and_valid():
    mod = load("ex15_until_connected")

    n = 20
    seed = 12345
    hg1, k1 = mod.grow_until_connected(n=n, seed=seed)

    # Node/edge sanity
    assert hg1.num_nodes() == n, (
        f"Hypergraph must have {n} nodes, got {hg1.num_nodes()}."
    )
    assert isinstance(k1, int) and k1 == hg1.num_edges(), (
        f"Reported number of added edges ({k1}) must equal hg.num_edges() ({hg1.num_edges()})."
    )

    # Connectivity
    lc = _largest_component_size(hg1)
    assert lc == n, (
        f"Hypergraph must be connected (largest component size {n}); got {lc}."
    )

    # Size constraints (2..4) and uniqueness
    sizes = _sizes(hg1)
    assert all(2 <= s <= 4 for s in sizes), (
        f"All added hyperedges must have size in [2,4]. Found sizes: {sorted(set(sizes))}."
    )
    es = _edge_set(hg1)
    assert len(es) == hg1.num_edges(), (
        f"Duplicate hyperedges detected: only {len(es)} unique edges out of {hg1.num_edges()}."
    )

    # Determinism under same seed
    hg2, k2 = mod.grow_until_connected(n=n, seed=seed)
    assert k2 == k1, (
        f"Same seed must produce the same number of edges. Expected {k1}, got {k2}."
    )
    assert _edge_set(hg2) == _edge_set(hg1), (
        "Same seed must reproduce the exact same set of hyperedges."
    )
