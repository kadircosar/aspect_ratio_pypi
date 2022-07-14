#!/usr/bin/env python
"""
Mapilio Calculation
"""
from __future__ import (absolute_import, division, print_function)

import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 5):
    raise RuntimeError(
        "Mapilio Calculation supports Python 3.6 and above. "
    )


INSTALL_REQUIRES = [
    'numpy',
]

setup(
    name="aspect_ratio_kd",
    version="0.0.1",
    description='Mapilio Calculation Library',
    url='https://github.com/mapilio/calculation.git',
    author='Mapilio - Ozcan Durak & MCV',
    author_email='ozcan@visiosoft.com.tr',
    license='licensed',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.6, <4",
    project_urls={  # Optional
            'Bug Reports': 'https://github.com/mapilio/calculation/issues',
            'Say Thanks!': 'https://mapilio.com/#contact',
            'Source': 'https://github.com/mapilio/calculation/',
        },
)