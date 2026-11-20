"""Copy the front page for 20 November 2026 to the output directory.

The entry image lives next to this script as ``entry.png``. This program
checks that the file is a real, complete PNG inside the competition's
limits — including recomputing the CRC of every chunk it contains — then
copies it byte for byte to ``$MAKEFUN_OUTPUT_DIR/entry.png`` (default
``/output``). It uses only the Python standard library and makes no
network requests, so both runs of the grader produce identical bytes.
"""

import os
import struct
import sys
import zlib

SOURCE_NAME = "entry.png"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
IEND_TRAILER = b"IEND\xaeB`\x82"


def _check_chunks(data):
    """Walk every PNG chunk and verify its CRC against its contents."""
    offset = len(PNG_MAGIC)
    seen_types = []
    while offset < len(data):
        if offset + 8 > len(data):
            raise ValueError("truncated chunk header in PNG")
        length, chunk_type = struct.unpack(">I4s", data[offset:offset + 8])
        body_start = offset + 8
        body_end = body_start + length
        if body_end + 4 > len(data):
            raise ValueError(
                f"chunk {chunk_type.decode('ascii', 'replace')} runs past end of file"
            )
        stored_crc, = struct.unpack(">I", data[body_end:body_end + 4])
        actual_crc = zlib.crc32(data[offset + 4:body_end]) & 0xFFFFFFFF
        if stored_crc != actual_crc:
            raise ValueError(
                f"chunk {chunk_type.decode('ascii', 'replace')} has a bad CRC "
                f"(stored {stored_crc:08x}, computed {actual_crc:08x})"
            )
        seen_types.append(chunk_type)
        offset = body_end + 4
    if not seen_types or seen_types[0] != b"IHDR":
        raise ValueError("PNG does not start with an IHDR chunk")
    if seen_types[-1] != b"IEND":
        raise ValueError("PNG does not end with an IEND chunk")
    return len(seen_types)


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
    if not data.endswith(IEND_TRAILER):
        raise ValueError(f"{path} is missing its IEND trailer")
    chunk_count = _check_chunks(data)
    print(f"{path}: {chunk_count} chunks, all CRCs valid")
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
