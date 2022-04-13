from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = long_description

setup(
    name="package",
    version=VERSION,
    license="MIT",
    author="Mark de Melo",
    author_email="mark.de-melo@arup.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    package_dir={"":"src"},
    install_requires=[],
    extras_require={},
    )