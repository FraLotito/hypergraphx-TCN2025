.PHONY: test test-solutions test-% test-solutions-%
PYTHON := $(shell command -v python >/dev/null 2>&1 && echo python || echo python3)

test:
	$(PYTHON) -m pytest -q

test-solutions:
	TARGET_PACKAGE=solutions $(PYTHON) -m pytest -q

# SPECIFIC FIRST so it isn't shadowed by test-%
test-solutions-%:
	TARGET_PACKAGE=solutions $(PYTHON) -m pytest -q -k "$*"

test-%:
	$(PYTHON) -m pytest -q -k "$*"
