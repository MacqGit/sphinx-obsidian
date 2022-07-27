# This file is needed for editable installs (`pip install -e .`).
# Can be removed once the following is resolved
# https://github.com/pypa/packaging-problems/issues/256
from setuptools import setup, find_packages
from pathlib import Path

# lines = Path("sphinx_obsidian").joinpath("__init__.py")
# for line in lines.read_text(encoding='utf-8').split("\n"):
#     if line.startswith("__version__ ="):
#         version = line.split(" = ")[-1].strip('"')
#         break

setup(
    name="sphinx-obsidian",
    version="0.0.1",
    python_requires=">=3.6",
    author="BE",
    author_email="bernard.etiennot@macq.eu",
    url="https://docs.macq.eu",
    project_urls={
        "Documentation": "https://docs.macq.eu",
    },
    # this should be a whitespace separated string of keywords, not a list
    keywords="Obsidian documentation",
    description="An Myst-Parser 'extension' to enable Obsidian MD to be compiled in Sphinx",
    long_description=Path("./README.md").read_text(encoding='utf-8'),
    long_description_content_type="text/markdown",
    license="MIT",
#    packages=['sphinx_obsidian', "sphinx_obsidian.wikilinks"],
#    Use rather:

    packages=find_packages(),
    install_requires=[
        'sphinx>=3,<5',
        'myst-parser'
    ],
    extras_require={
        'sphinx': [
            "sphinx~=4.4",  # Force Sphinx to be the latest version
        ],
    },
    include_package_data=True,

)