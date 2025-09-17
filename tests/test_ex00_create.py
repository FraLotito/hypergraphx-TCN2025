from tests.helpers import load

def test_counts_and_membership():
    mod = load("ex00_create")
    hg = mod.build_hypergraph_hgx()

    assert hg.num_nodes() == 8, (
        f"Wrong number of nodes: expected 8, got {hg.num_nodes()}. "
        f"Nodes present: {sorted(map(str, hg.get_nodes()))}"
    )
    assert hg.num_edges() == 5, (
        f"Wrong number of hyperedges: expected 5, got {hg.num_edges()}."
    )

    # Sanity: all edge members must belong to the node set
    node_set = set(map(str, hg.get_nodes()))
    for e in hg.get_edges():
        e_nodes = set(map(str, e))
        missing = e_nodes - node_set
        assert not missing, (
            "Edge contains nodes not in the hypergraph's node set. "
            f"Edge: {tuple(sorted(e_nodes))} | Missing in node set: {sorted(missing)}"
        )
