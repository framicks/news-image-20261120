"""Copy the front page for 20 November 2026 to the output directory.

The entry image lives next to this script as ``entry.png``. This program
checks that the file is a real, complete PNG inside the competition's
limits, then copies it byte for byte to ``$MAKEFUN_OUTPUT_DIR/entry.png``
(default ``/output``). It uses only the Python standard library and makes
no network requests, so both runs of the grader produce identical bytes.
"""

import os
import struct
import sys

SOURCE_NAME = "entry.png"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def read_png(path):
    """Return the file's bytes after confirming it is a whole PNG."""
    with open(path, "rb") as handle:
        data = handle.read()
    if len(data) > MAX_BYTES:
        raise ValueError(f"{path} is {len(data)} bytes, over the 1 MiB limit")
    if not data.startswith(PNG_MAGIC):
        raise ValueError(f"{path} does not start with the PNG signature")
    if len(data) < 33:
        raise ValueError(f"{path} is too short to hold a PNG header")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError(f"image is {width}x{height}, over 1024x1024")
    if not data.endswith(b"IEND\xaeB`\x82"):
        raise ValueError(f"{path} is missing its IEND trailer")
    return data


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    blob = read_png(source)
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, SOURCE_NAME)
    with open(target, "wb") as handle:
        handle.write(blob)
    print(f"wrote {target} ({len(blob)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
