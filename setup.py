#!/usr/bin/env python3
from pathlib import Path

import setuptools
from setuptools import setup

this_dir = Path(__file__).parent

requirements = []
requirements_path = this_dir / "requirements.txt"
if requirements_path.is_file():
    with open(requirements_path, "r", encoding="utf-8") as requirements_file:
        requirements = requirements_file.read().splitlines()

module_dir = this_dir / "wyoming_porcupine3"
data_dir = module_dir / "data"
data_files = list(data_dir.rglob("*.pv")) + list(data_dir.rglob("*.ppn"))

# -----------------------------------------------------------------------------

setup(
    name="wyoming_porcupine3",
    version="1.0.1",
    description="Wyoming Server for Porcupine 1",
    url="http://github.com/rhasspy/wyoming-porcupine3",
    author="Michael Hansen",
    author_email="mike@rhasspy.org",
    license="MIT",
    packages=setuptools.find_packages(),
    package_data={
        "wyoming_porcupine3": [str(p.relative_to(module_dir)) for p in data_files]
    },
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="rhasspy wyoming porcupine wake word",
)
