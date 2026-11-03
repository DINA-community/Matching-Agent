import hashlib
import json
from typing import Any


def hash_matching_config(config: dict[str, Any]) -> str:
    """Generate a hash from matching configuration dictionary.

    The hash is computed from a canonical JSON representation of the config
    to ensure consistent hashing regardless of key ordering.

    Args:
        config: The matching configuration dictionary

    Returns:
        A short hash string (first 16 characters of SHA256)
    """
    canonical_json = json.dumps(config, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical_json.encode()).hexdigest()[:16]


def get_default_config_hash() -> str:
    """Get the hash for the default matching configuration.

    This loads the default config from the standard location and computes its hash.
    """
    import tomllib
    from pathlib import Path

    config_path = Path("./assets/plugin_configs/default/matching_config.toml")
    with open(config_path, "rb") as f:
        config = tomllib.load(f)
    return hash_matching_config(config)
