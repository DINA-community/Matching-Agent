# Configuration file for the Sphinx documentation builder.
#
# This configuration aims to auto-generate documentation from the
# project's Python docstrings. It assumes the package source lives under
# the "src" directory and the top-level package is "dina".

from __future__ import annotations

import os
import sys
from pathlib import Path

# -- Path setup --------------------------------------------------------------
# Add the project src directory to sys.path so autodoc can import the code.
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

# -- Project information -----------------------------------------------------
project = "dina.matcher"

# Try to determine version from pyproject.toml, falling back to package/distribution metadata.
# We keep this resilient to allow local docs builds without installing the package.
release = "0.1.0"
version = release

try:
    import tomllib  # Python 3.11+
except Exception:  # pragma: no cover
    tomllib = None  # type: ignore

pyproject_toml = ROOT / "pyproject.toml"
if tomllib and pyproject_toml.exists():
    try:
        data = tomllib.loads(pyproject_toml.read_text(encoding="utf-8"))
        project_table = data.get("project") or {}
        rel = project_table.get("version")
        if isinstance(rel, str):
            release = rel
            version = rel
        name = project_table.get("name")
        if isinstance(name, str):
            project = name
    except Exception:
        pass
else:
    # Last resort: try importlib.metadata if the package is installed
    try:
        from importlib.metadata import version as _dist_version

        release = _dist_version(project)
        version = release
    except Exception:
        pass

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

autosummary_generate = True
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_attr_annotations = True

# Make autodoc include members by default
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "inherited-members": True,
}

# Patterns to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = os.getenv("SPHINX_HTML_THEME", "furo")
html_title = f"{project} {release} documentation"

templates_path = ["_templates"]
