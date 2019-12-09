#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

NAME = "foo"


install_requires = []

tests_requires = ["pytest", "pytest-cov", "numpy"]
style_requires = ["flake8", "wemake-python-styleguide", "mypy", "black==19.3b0"]
dev_requires = tests_requires + style_requires

setup(
    name=NAME,
    description="foo",
    author="dabljues",
    author_email="dabljues96@gmail.com",
    url="https://github.com/dabljues/flake8_error",
    license="BSD",
    install_requires=install_requires,
    packages=find_packages(exclude=("tests")),
    extras_require={"dev": dev_requires, "tests": tests_requires, "style": style_requires},
)
