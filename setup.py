#!/usr/bin/env python3


# +
# import(s)
# -
import setuptools


# +
# read file
# -
with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]

# +
# setup
# -
setuptools.setup(
    name="sassy_q3c_models",
    version="1.7.3",
    author="Phil Daly",
    author_email="pndaly@arizona.edu",
    description="Pythonic object request models (ORMs) for the SASSyII database tables (mainly) using Q3C indexing ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SAGUARO-MMA/sassy_q3c_models",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent", ],
    python_requires='>=3.6',
)
