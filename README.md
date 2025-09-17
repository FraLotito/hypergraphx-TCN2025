# The Threads of Complex Networks — TCN2025  
**Summer School • Firenze (Florence) • 16–19 settembre 2025**

Hands-on materials for **Hypergraphx (HGX)**: programming exercises, tests and runnable notebooks.
You’ll generate hypergraphs, compute statistics, build projections, generate random hypergraphs, compute motifs and detect communities.

---

## Quick start

```bash
pip install -r requirements.txt
make test               # run tests against exercises/
make test-solutions     # run tests against reference solutions
```

---

## Run a single test (pattern targets)

Usage examples:

```bash
make test-ex01                  # run tests matching “ex01” against exercises/
make test-solutions-ex01        # run tests matching “ex01” against solutions/
make test-components            # e.g., anything matching “components”
```

---

## Datasets

Place JSON datasets under **`datasets/`** (repo root). Examples used here:

- `contacts-high-school.json`
- `coauth-cs-NeurIPS.json`
- `NDC-classes.json`

Set your path in notebooks or scripts like:

```python
DATASET_PATH = "../datasets/contacts-high-school.json" or
DATASET_PATH = "datasets/contacts-high-school.json"
```

---

## What’s inside (high level)

- **Exercises** (`exercises/…`) — each file has a short statement and function stubs that raise `NotImplementedError("Implement me!")`.
- **Solutions** (`solutions/…`) — reference implementations (validated by the same tests).
- **Tests** (`tests/…`) — descriptive failure messages to guide debugging.
- **Notebooks** (`notebooks-exercises/…`, `notebooks-solutions/…`) — runnable Jupyter notebooks with hints or full solutions.

Key topics:

- Building & inspecting HGX hypergraphs
- **Connected components** using HGX built‑ins
- Participation by edge size
- **Degree ranks** and sensitivity to adding edges
- **Random generation** with `hypergraphx.generation.random.random_hypergraph`
- Growing until **connected** (sizes 2–4), seeded & reproducible
- Loading datasets and reporting **(#nodes, #edges)**
- **Projections** with `clique_projection(h, keep_isolated=False)`
- **Motifs** (exact counts/profile)
- **Communities** (mandatory): detect on the 2‑clique projection or via HGX’s community API if available; report community counts and size distribution

---

## Tips

- Prefer **HGX APIs** over ad‑hoc code:
  - Components: `hg.connected_components()`, `hg.largest_component_size()`
  - Size distribution: `hg.distribution_sizes()`
  - Generation: `random_hypergraph(num_nodes, num_edges_by_size, seed=...)`
  - Projections: `clique_projection(h, keep_isolated=False)`
  - Visualization: `hypergraphx.viz.draw_hypergraph.draw_hypergraph(h)`
- Keep outputs deterministic (sort node labels where required, seed your generators).
- Tests often expect **string node labels** and **sorted lists** for reproducibility.

---

## Acknowledgements

Materials prepared for The Threads of Complex Networks (TCN2025) — Firenze, 16–19 settembre 2025.

### Have fun and explore!