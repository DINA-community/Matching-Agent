# Minimal Makefile for Sphinx documentation
#
# Use: make html
# This Makefile uses `uv` to run the Sphinx build with the dev dependency group.

SPHINXOPTS    =
SPHINXBUILD   = uv run --group dev sphinx-build
SOURCEDIR     = ./docs
BUILDDIR      = ./docs/_build

.PHONY: help clean docs

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

clean:
	rm -rf "$(BUILDDIR)"

docs:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
