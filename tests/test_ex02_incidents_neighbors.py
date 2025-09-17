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

def test_incident_edges_sorted_and_neighbors_by_size():
    mod = load("ex02_incidents_neighbors")
    hg = _make_hg()

    inc_A = mod.incident_edges(hg, "A")
    expected_inc_A = [("A","B","C"), ("A","D"), ("A","E","H")]
    assert inc_A == expected_inc_A, (
        "Incorrect incident edges for node 'A' or ordering not respected. "
        f"Expected {expected_inc_A}, got {inc_A}. "
        "Each tuple must be sorted, and the list must be sorted."
    )

    expected_nbrs_A_s3 = {"B","C","E","H"}
    nbrs_A_s3 = mod.neighbors_by_size(hg, "A", 3)
    assert nbrs_A_s3 == expected_nbrs_A_s3, (
        "Wrong neighbors for node 'A' when filtering by edge size = 3. "
        f"Expected {expected_nbrs_A_s3}, got {nbrs_A_s3}."
    )

def test_largest_component_size():
    mod = load("ex02_incidents_neighbors")
    hg = _make_hg()
    size = mod.largest_component_size(hg)
    assert size == 8, (
        f"Wrong largest component size. Expected 8, got {size}."
    )
