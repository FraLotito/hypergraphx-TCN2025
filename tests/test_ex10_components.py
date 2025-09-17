from tests.helpers import load
from hypergraphx.core.hypergraph import Hypergraph

def _toy_one_component():
    hg = Hypergraph()
    hg.add_nodes(list("ABCDEFGH"))
    hg.add_edges([
        ("A","B","C"),
        ("B","C","D"),
        ("A","D"),
        ("E","F","G"),
        ("A","E","H"),
    ])  # All nodes are connected via hyperedges
    return hg

def _toy_multiple_components_with_isolate():
    hg = Hypergraph()
    hg.add_nodes(list("ABCDEFGH"))
    # Remove the bridging edge ("A","E","H") so the graph splits:
    # {A,B,C,D}, {E,F,G}, and {"H"} (isolated node still counted as a component)
    hg.add_edges([
        ("A","B","C"),
        ("B","C","D"),
        ("A","D"),
        ("E","F","G"),
    ])
    return hg

def _is_sorted_list_of_strs(lst):
    return isinstance(lst, list) and all(isinstance(x, str) for x in lst) and lst == sorted(lst)

def test_components_and_largest_size_one_component():
    mod = load("ex10_components")
    hg = _toy_one_component()

    comps = mod.components(hg)
    assert isinstance(comps, list) and all(isinstance(c, list) for c in comps), (
        f"'components' must return a list of lists. Got: {type(comps)} with element types {[type(c) for c in comps]}"
    )
    # Each component list should be sorted strings
    for c in comps:
        assert _is_sorted_list_of_strs(c), (
            f"Each component must be a sorted list of strings. Bad component: {c}"
        )

    # Expect a single component covering all 8 nodes
    got_sets = {frozenset(c) for c in comps}
    expected_sets = {frozenset("ABCDEFGH")}
    assert got_sets == expected_sets, (
        f"Wrong components for the single-component toy graph. "
        f"Expected {sorted(map(list, expected_sets))}, got {sorted(map(list, got_sets))}."
    )

    size = mod.largest_component_size(hg)
    assert size == 8, (
        f"Largest component size should be 8, got {size}."
    )

def test_components_and_largest_size_multiple_components():
    mod = load("ex10_components")
    hg = _toy_multiple_components_with_isolate()

    comps = mod.components(hg)
    assert isinstance(comps, list) and all(isinstance(c, list) for c in comps), (
        f"'components' must return a list of lists. Got: {type(comps)} with element types {[type(c) for c in comps]}"
    )
    for c in comps:
        assert _is_sorted_list_of_strs(c), (
            f"Each component must be a sorted list of strings. Bad component: {c}"
        )

    got_sets = {frozenset(c) for c in comps}
    expected_sets = {
        frozenset("ABCD"),
        frozenset("EFG"),
        frozenset("H"),
    }
    assert got_sets == expected_sets, (
        "Wrong components for the multi-component toy graph. "
        f"Expected {sorted(map(list, expected_sets))}, got {sorted(map(list, got_sets))}."
    )

    size = mod.largest_component_size(hg)
    assert size == 4, (
        f"Largest component size should be 4 (component ABCD), got {size}."
    )
