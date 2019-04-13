from pathlib import Path

from setuptools import find_packages, setup


HERE = Path(__file__).parent.resolve()


setup(
    name="text-editor",
    version="1.0.5",
    description="Like webbrowser, but for the text editor.",
    long_description=(HERE / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Juan-Pablo Scaletti",
    author_email="juanpablo@jpscaletti.com",
    python_requires=">=3.5,<4.0",
    url="https://github.com/jpscaletti/texteditor",
    # install_requires=[],
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
