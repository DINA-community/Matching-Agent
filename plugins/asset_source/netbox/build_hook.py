from __future__ import annotations

import logging
import shutil
import subprocess
import tempfile
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

logger = logging.getLogger(__name__)


def generate_api_client(spec_path: Path, output_parent_dir: Path) -> None:
    """
    Generate the Python API client using openapi-generator-cli into a temporary
    directory, then copy only the package directory (e.g., `netbox_api_client`)
    into the provided output_parent_dir.

    Args:
        spec_path: Path to the OpenAPI/Swagger spec (json/yaml).
        output_parent_dir: Directory where the package directory should be placed.
    """
    if not spec_path.exists():
        raise FileNotFoundError(f"Spec file not found: {spec_path}")

    # Ensure parent exists
    output_parent_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Generating Netbox API client from %s", spec_path)

    with tempfile.TemporaryDirectory(prefix="netbox_codegen_") as tmpdir:
        tmp_out = Path(tmpdir)
        cmd = [
            "openapi-python-client",
            "generate",
            "--path",
            str(spec_path),
            "--output-path",
            str(tmp_out),
            "--overwrite",
            "--custom-template-path",
            str(spec_path.parent / "api_templates"),
        ]

        logger.debug("Running command: %s", " ".join(cmd))
        try:
            subprocess.run(cmd, check=True)
        except FileNotFoundError as e:
            raise RuntimeError(
                "openapi-generator-cli not found. Ensure it is installed and available in PATH."
            ) from e

        package_name = "net_box_rest_api_client"
        candidates = [tmp_out / package_name]
        pkg_src: Path | None = next((c for c in candidates if c.exists()), None)
        if pkg_src is None:
            # Fallback: search for directory named package_name
            for p in tmp_out.rglob(package_name):
                if p.is_dir():
                    pkg_src = p
                    break
        if pkg_src is None:
            raise RuntimeError(
                f"Failed to locate generated package directory '{package_name}' in {tmp_out}"
            )

        target_pkg_dir = output_parent_dir / "api_client"
        if target_pkg_dir.exists():
            logger.info("Removing existing generated package at %s", target_pkg_dir)
            shutil.rmtree(target_pkg_dir)

        logger.info("Copying generated package from %s to %s", pkg_src, target_pkg_dir)
        shutil.copytree(pkg_src, target_pkg_dir)


class BuildHook(BuildHookInterface):
    """Hatchling build hook that generates the Netbox API client at build time."""

    def initialize(self, version: str, build_data: dict) -> None:  # type: ignore[override]
        project_root = Path(self.root)
        # Locate the swagger spec bundled with the plugin
        spec = project_root / "assets" / "netbox-api.yaml"

        output_parent = (
            project_root
            / "src"
            / "dina"
            / "plugins"
            / "datasource"
            / "netbox"
            / "generated"
        )

        logger.info("Using spec: %s", spec)
        logger.info("Output directory (parent): %s", output_parent)

        generate_api_client(spec, output_parent)
        logger.info("Netbox API client generation completed.")
