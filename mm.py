#!/usr/bin/env python
"""
COPY THIS FILE TO YOUR PROJECT.
---------
This file generates all the necessary files for packaging for the project.
Read more about it at https://github.com/jpscaletti/mastermold/
"""
from pathlib import Path

import copier
from ruamel.yaml import YAML


data = {
    "title": "TextEditor",
    "name": "texteditor",
    "pypi_name": "text-editor",
    "version": "1.0.5",
    "author": "Juan-Pablo Scaletti",
    "author_email": "juanpablo@jpscaletti.com",
    "description": "Like webbrowser, but for the text editor.",
    "repo_name": "jpscaletti/texteditor",
    "home_url": "",
    "docs_url": "",
    "development_status": "5 - Production/Stable",
    "install_requires": [],
    "entry_points": "",
    "minimal_python": 3.5,

    "coverage_omit": [],

    "has_docs": False,
    "docs_nav": [],  # Overwritten by `save_current_nav`.
}


def save_current_nav():
    yaml = YAML()
    mkdocs_path = Path("docs") / "mkdocs.yml"
    if not mkdocs_path.exists():
        return
    mkdocs = yaml.load(mkdocs_path)
    data["docs_nav"] = mkdocs.get("nav")


def do_the_thing():
    if data["has_docs"]:
        save_current_nav()

    copier.copy(
        "gh:jpscaletti/mastermold.git",
        ".",
        data=data,
        exclude=[
            "copier.yml",
            "README.md",
            ".git",
            ".git/*",
            ".venv",
            ".venv/*",

            "docs",
            "docs/*",
            "CONTRIBUTING.md",
        ],
        force=True,
        cleanup_on_error=False
    )


if __name__ == "__main__":
    do_the_thing()
