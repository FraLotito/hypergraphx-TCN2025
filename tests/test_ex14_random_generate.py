from tests.helpers import load
from hypergraphx.core.hypergraph import Hypergraph

SIZES = [2, 3, 4, 5, 6]

def _size_hist(hg: Hypergraph):
    hist = {}
    for e in hg.get_edges():
        s = len(e)
        hist[s] = hist.get(s, 0) + 1
    return hist

def _edge_set(hg: Hypergraph):
    return {frozenset(map(str, e)) for e in hg.get_edges()}

def test_five_majority_minimums_and_seed():
    mod = load("ex14_random_generate")

    n_min, e_min = 12, 10   # ensure sizes up to 6 are feasible
    seed = 2025

    hgs = mod.generate_five_majority(n_min=n_min, e_min=e_min, seed=seed)
    assert isinstance(hgs, list) and len(hgs) == 5, (
        f"Expected a list of 5 hypergraphs, got type={type(hgs)}, len={len(hgs) if isinstance(hgs, list) else 'N/A'}."
    )

    edge_sets = []
    for i, target in enumerate(SIZES):
        hg = hgs[i]
        assert isinstance(hg, Hypergraph), (
            f"hgs[{i}] is not a Hypergraph instance (got {type(hg)})."
        )
        assert hg.num_nodes() >= n_min, (
            f"hgs[{i}] must have at least {n_min} nodes, got {hg.num_nodes()}."
        )
        assert hg.num_edges() >= e_min, (
            f"hgs[{i}] must have at least {e_min} hyperedges, got {hg.num_edges()}."
        )

        hist = _size_hist(hg)
        target_count = hist.get(target, 0)
        other_max = max([hist.get(s, 0) for s in SIZES if s != target], default=0)
        assert target_count > other_max, (
            f"hgs[{i}] does not have a strict majority of size {target}. "
            f"Counts: target={target_count}, others_max={other_max}, full_hist={hist}."
        )

        # record edge set for determinism check
        edge_sets.append(_edge_set(hg))

    # Determinism: same seed -> same five edge sets
    hgs2 = mod.generate_five_majority(n_min=n_min, e_min=e_min, seed=seed)
    for i in range(5):
        assert _edge_set(hgs2[i]) == edge_sets[i], (
            f"With the same seed, hgs2[{i}] edge set differs from hgs[{i}]."
        )
