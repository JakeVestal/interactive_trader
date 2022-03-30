# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="interactive_trader",
    version="0.1.0",
    description="Trade on Interactive Brokers with Plotly Dash in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://interactive-trader.readthedocs.io/",
    author="Jake Vestal",
    author_email="jmv13@duke.edu",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["medium_multiply"],
    include_package_data=True,
    install_requires=["pandas", "dash", "ibapi"]
)