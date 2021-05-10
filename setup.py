# Copyright 2021 John Joowon Lee. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or  implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Setuptools installation script."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import find_packages
from setuptools import setup

description = """nii_ag is a library for building models of aerobic glycolysis in
Graph Nets, Sonnet and Tensorflow.
"""

setup(
    name="nii_ag",
    version="0.0.0.dev",
    description="Library for building models of aerobic glycolysis in Graph Nets, Sonnet and Tensorflow",
    long_description=description,
    author="John Joowon Lee",
    license="Apache License, Version 2.0",
    keywords=["aerobic glycolysis", "PET", "graph networks", "tensorflow", "sonnet", "machine learning"],
    url="https://github.com/jjleewustledu/nii_ag",
    packages=find_packages(),
    # Additional "tensorflow" and "tensorflow_probability" requirements should
    # be installed separately (See README).
    install_requires=[
        "graph-nets",
        "absl-py",
        "dm-sonnet",
        "dm-tree",
        "future",
        "networkx",
        "numpy",
        "setuptools",
        "six",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3.4",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
