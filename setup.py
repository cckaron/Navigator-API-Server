# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "Wayfic_Api_Server"
VERSION = "0.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["flask", "connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Navigator Sharing Data",
    author_email="cckaron28@gmail.com",
    url="",
    install_requires=REQUIRES,
)
