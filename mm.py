#!/usr/bin/env python
"""
This file generates all the necessary files for packaging for the project.
Read more about it at https://github.com/jpscaletti/mastermold/
"""
data = {
    "title": "TextEditor",
    "name": "texteditor",
    "pypi_name": "texteditor",
    "version": "1.0.6",
    "author": "Juan-Pablo Scaletti",
    "author_email": "juanpablo@jpscaletti.com",
    "description": "Like webbrowser, but for the text editor.",
    "copyright": "2019",
    "repo_name": "jpscaletti/texteditor",
    "home_url": "",
    "project_urls": {
    },
    "development_status": "5 - Production/Stable",
    "minimal_python": 3.5,
    "install_requires": [
    ],
    "testing_requires": [
        "pytest",
    ],
    "development_requires": [
        "tox",
        "flake8",
    ],
    "entry_points": "",

    "coverage_omit": [],
}

exclude = [
    "hecto.yml",
    "README.md",
    ".git",
    ".git/*",
    ".venv",
    ".venv/*",
    "CONTRIBUTING.md",
]


def do_the_thing():
    import hecto

    hecto.copy(
        # "gh:jpscaletti/mastermold.git",
        "../mastermold",  # Path to the local copy of Master Mold
        ".",
        data=data,
        exclude=exclude,
        force=False,
    )


if __name__ == "__main__":
    do_the_thing()
