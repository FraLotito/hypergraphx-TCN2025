import os
import pytest
from tests.helpers import load
from hypergraphx.readwrite import load_hypergraph

DATA_DIR = "datasets"

DATASETS = [
    "contacts-high-school.json",
    "coauth-cs-NeurIPS.json",
    "NDC-classes.json",
]

def _path(name: str) -> str:
    return os.path.join(DATA_DIR, name)

def _skip_if_missing(path: str):
    if not os.path.exists(path):
        pytest.skip(f"Dataset not found: {path} — add it under 'data/' to run this test.")

@pytest.mark.parametrize("fname", DATASETS)
def test_load_and_counts(fname):
    mod = load("ex13_load_counts")
    path = _path(fname)
    _skip_if_missing(path)

    # Ground-truth via HGX
    hg_truth = load_hypergraph(path)
    nodes_truth = hg_truth.num_nodes()
    edges_truth = hg_truth.num_edges()

    # Student implementation (single function)
    nodes, edges = mod.load_counts(path)

    assert isinstance(nodes, int) and isinstance(edges, int), (
        f"{fname}: counts must be integers. Got types: nodes={type(nodes)}, edges={type(edges)}."
    )
    assert nodes == nodes_truth, (
        f"{fname}: wrong number of nodes. Expected {nodes_truth}, got {nodes}."
    )
    assert edges == edges_truth, (
        f"{fname}: wrong number of edges. Expected {edges_truth}, got {edges}."
    )
