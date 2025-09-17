from tests.helpers import load
from hypergraphx.core.hypergraph import Hypergraph

def _toy():
    hg = Hypergraph()
    hg.add_nodes(list("ABCDEFGH"))  # 8 nodes
    hg.add_edges([
        ("A","B","C"), ("B","C","D"), ("A","D"), ("E","F","G"), ("A","E","H")
    ])  # sizes: 3,3,2,3,3
    return hg

def test_buckets_and_shares():
    mod = load("ex05_size_coverage")
    hg = _toy()

    buckets = mod.edge_size_buckets(hg)
    assert buckets == {2: 1, 3: 4}, (
        f"Wrong edge size buckets. Expected {{2:1, 3:4}}, got {buckets}."
    )

    covered = mod.nodes_covered_by_size(hg)
    exp_cov_2 = {"A","D"}
    exp_cov_3 = {"A","B","C","D","E","F","G","H"}
    assert covered.get(2) == exp_cov_2, (
        f"Nodes covered by size-2 edges incorrect. Expected {sorted(exp_cov_2)}, "
        f"got {sorted(covered.get(2, set()))}."
    )
    assert covered.get(3) == exp_cov_3, (
        f"Nodes covered by size-3 edges incorrect. Expected all 8 nodes, got "
        f"{sorted(covered.get(3, set()))}."
    )

    shares = mod.coverage_share_by_size(hg)
    assert abs(shares.get(2, 0.0) - 0.25) < 1e-9, (
        f"Share for size-2 edges should be 0.25 (2 of 8 nodes), got {shares.get(2)}."
    )
    assert abs(shares.get(3, 0.0) - 1.0) < 1e-9, (
        f"Share for size-3 edges should be 1.0 (all 8 nodes), got {shares.get(3)}."
    )

    cum = mod.cumulative_coverage_share(hg, ascending=True)
    # ascending sizes: first 2 -> 0.25, then 3 -> 1.0
    assert list(cum.keys()) == [2, 3], (
        f"Cumulative keys (ascending) should be [2, 3], got {list(cum.keys())}."
    )
    assert abs(cum[2] - 0.25) < 1e-9 and abs(cum[3] - 1.0) < 1e-9, (
        f"Cumulative shares incorrect. Expected {{2:0.25, 3:1.0}}, got {cum}."
    )
