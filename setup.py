from setuptools import setup, find_packages

__version__ = "2.0.1"

setup(
    name="request-api-builder",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
