from __future__ import annotations

import logging
import shutil
import subprocess
import tempfile
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

logger = logging.getLogger(__name__)

DEF_PACKAGE_NAME = "dina.plugins.datasource.isduba.generated.isduba_api_client"


def generate_api_client(
    spec_path: Path, output_parent_dir: Path, package_path: str = DEF_PACKAGE_NAME
) -> None:
    """
    Generate the Python API client using openapi-generator-cli into a temporary
    directory, then copy only the package directory (e.g., `isduba_api_client`)
    into the provided output_parent_dir.

    Args:
        spec_path: Path to the OpenAPI/Swagger spec (json/yaml).
        output_parent_dir: Directory where the package directory should be placed.
        package_path: The name for the generated python package.
    """
    if not spec_path.exists():
        raise FileNotFoundError(f"Spec file not found: {spec_path}")

    # Ensure parent exists
    output_parent_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Generating ISDuBA API client from %s", spec_path)

    with tempfile.TemporaryDirectory(prefix="isduba_codegen_") as tmpdir:
        tmp_out = Path(tmpdir)
        cmd = [
            "openapi-generator-cli",
            "generate",
            "-i",
            str(spec_path),
            "-g",
            "python",
            "-o",
            str(tmp_out),
            "--package-name",
            package_path,
            "--library",
            "asyncio",
        ]

        logger.debug("Running command: %s", " ".join(cmd))
        try:
            subprocess.run(cmd, check=True)
        except FileNotFoundError as e:
            raise RuntimeError(
                "openapi-generator-cli not found. Ensure it is installed and available in PATH."
            ) from e

        split_package_path = package_path.split(".")
        package_name = split_package_path[-1]
        package_path = "/".join(split_package_path)
        # Locate the generated package directory (may be under src/<pkg> or at root)
        candidates = [
            tmp_out / "src" / package_path,
            tmp_out / package_path,
        ]
        pkg_src: Path | None = next((c for c in candidates if c.exists()), None)
        if pkg_src is None:
            # Fallback: search for directory named package_name
            for p in tmp_out.rglob(package_path):
                if p.is_dir():
                    pkg_src = p
                    break
        if pkg_src is None:
            raise RuntimeError(
                f"Failed to locate generated package directory '{package_path}' in {tmp_out}"
            )

        target_pkg_dir = output_parent_dir / package_name
        if target_pkg_dir.exists():
            logger.info("Removing existing generated package at %s", target_pkg_dir)
            shutil.rmtree(target_pkg_dir)

        logger.info("Copying generated package from %s to %s", pkg_src, target_pkg_dir)
        shutil.copytree(pkg_src, target_pkg_dir)


class BuildHook(BuildHookInterface):
    """Hatchling build hook that generates the ISDuBA API client at build time."""

    def initialize(self, version: str, build_data: dict) -> None:  # type: ignore[override]
        project_root = Path(self.root)
        # Locate the swagger spec bundled with the plugin
        spec = project_root / "assets" / "isduba-api.json"

        output_parent = (
            project_root
            / "src"
            / "dina"
            / "plugins"
            / "datasource"
            / "isduba"
            / "generated"
        )

        logger.info("Using spec: %s", spec)
        logger.info("Output directory (parent): %s", output_parent)

        generate_api_client(spec, output_parent, DEF_PACKAGE_NAME)
        logger.info("ISDuBA API client generation completed.")
