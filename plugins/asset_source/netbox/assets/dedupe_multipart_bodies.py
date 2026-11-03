#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Remove redundant and failing `multipart/form-data` request bodies from the NetBox OpenAPI spec.

The OpenAPI schema declares for every write endpoint two possible body types:
- `application/json`, and
- `multipart/form-data`
Their content is basically identical.

`openapi-python-client` (version 0.29.0 and 0.29.1) mishandles this:
https://github.com/openapi-generators/openapi-python-client/issues/1451
For all Multi-body endpoints, it emits a function signature using `| Unset`,
but without importing the required `Unset` type
That results in `NameError`s for all endpoints.

As a workaround, we remove the sections triggering the bug from the OpenAPI spec file.

The script does not parse and write the entire document with a YAML library,
because that can cause reordering and reformatting.
It only removes the `multipart/form-data` blocks where the content is identical to the same `application/json` block.
At the moment, all `application/json` blocks are identical to the `multipart/form-data` blocks,
but there is no guarantee this will stay so in the future.

Usage:
    # modify in place:
    ./dedupe_multipart_bodies.py <path-to-spec.yaml>
    # write to a new file:
    ./dedupe_multipart_bodies.py <path-to-spec.yaml> -o out.yaml
"""

import argparse
import re
import sys
from pathlib import Path

# 1. Matches a `requestBody:` block's `content:` section (indented by 8 spaces)
# 2. matches exactly one `application/json:` in it (with 10 space indent)
# 3. followed the `multipart/form-data:` block (with the same 10 space indent)
PATTERN = re.compile(
    r"(?P<indent>[ ]{8})content:\n"
    r"(?P<indent10>[ ]{10})application/json:\n"
    r"(?P<json_body>(?:(?P=indent10)[ ].*\n)+)"
    r"(?P=indent10)multipart/form-data:\n"
    r"(?P<multipart_body>(?:(?P=indent10)[ ].*\n)+)"
)


def dedupe(spec_text: str) -> tuple[str, int]:
    """Removes `multipart/form-data` blocks that are identical to the `application/json` block.

    Returns the modified spec text and the number of blocks removed.
    """
    removed = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal removed
        if match.group("json_body") != match.group("multipart_body"):
            # Differening blocks don't trigger the bug, leave them as is
            # Return the whole match, unchanged
            return match.group(0)
        removed += 1
        # return only the json block
        return f"{match.group('indent')}content:\n{match.group('indent10')}application/json:\n{match.group('json_body')}"

    # Apply the replacment function to the entire file
    new_text = PATTERN.sub(replace, spec_text)
    return new_text, removed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("spec", type=Path, help="Path to the OpenAPI spec YAML file")
    parser.add_argument("-o", "--output", type=Path, default=None, help="Write result here instead of modifying in place")
    args = parser.parse_args()

    original = args.spec.read_text(encoding="utf-8")
    updated, removed = dedupe(original)

    if removed == 0:
        print("Nothing to do.", file=sys.stderr)
    else:
        print(f"Removed {removed} duplicate multipart/form-data block(s).", file=sys.stderr)

    out_path = args.output if args.output else args.spec
    out_path.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
