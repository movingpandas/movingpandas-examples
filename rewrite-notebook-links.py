#!/usr/bin/env python3
"""Rewrite relative notebook links in generated HTML to HTML links."""

from __future__ import annotations

import argparse
import re
from collections.abc import Iterable
from pathlib import Path


LOCAL_NOTEBOOK_HREF = re.compile(
    r"""
    (?P<prefix>\bhref\s*=\s*)
    (?P<quote>["'])
    (?P<path>
        (?![a-zA-Z][a-zA-Z0-9+.-]*:)  # URL with a scheme
        (?!//)                         # protocol-relative URL
        (?!/)                          # site-root-relative URL
        (?!\#)                         # fragment-only link
        [^"'?#]+?
    )
    \.ipynb
    (?P<suffix>[?#][^"']*)?
    (?P=quote)
    """,
    re.VERBOSE | re.IGNORECASE,
)


def rewrite_file(path: Path) -> int:
    """Rewrite local notebook hrefs in *path* and return the replacement count."""
    original = path.read_text(encoding="utf-8")
    rewritten, replacements = LOCAL_NOTEBOOK_HREF.subn(
        lambda match: (
            f"{match['prefix']}{match['quote']}"
            f"{match['path']}.html{match['suffix'] or ''}"
            f"{match['quote']}"
        ),
        original,
    )
    if replacements:
        path.write_text(rewritten, encoding="utf-8")
    return replacements


def find_html_files(paths: Iterable[Path]) -> list[Path]:
    """Return unique HTML files found in explicit files and directories."""
    html_files: set[Path] = set()
    for path in paths:
        if path.is_dir():
            html_files.update(path.rglob("*.html"))
        elif path.is_file() and path.suffix.lower() == ".html":
            html_files.add(path)
        else:
            raise ValueError(f"Not an HTML file or directory: {path}")
    return sorted(html_files)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="HTML files or directories containing generated HTML files",
    )
    args = parser.parse_args()

    total_replacements = 0
    for html_file in find_html_files(args.paths):
        replacements = rewrite_file(html_file)
        total_replacements += replacements
        if replacements:
            print(f"{html_file}: rewrote {replacements} link(s)")

    print(f"Rewrote {total_replacements} link(s)")


if __name__ == "__main__":
    main()
