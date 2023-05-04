import os
from setuptools import setup

from octoclient import __version__

cwd = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(cwd, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="octoclient",
    version=__version__,
    description="A lightweight client for the OctoPrint REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pnpolcher/octoclient",
    author="Pablo Nuñez Pölcher",
    author_email="info@pablopolcher.dev",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="octoclient octoprint client",
    packages=["octoclient"],
    python_requires=">=3.7, <4",
    install_requires=[
        "setuptools==67.7.2"
    ],
    extras_require={
        "dev": ["flake8==6.0.0", "nose2==0.13.0"]
    },
)