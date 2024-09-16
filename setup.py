"""Setuptools entry point."""
import os
from setuptools import setup, find_packages
import pytest_splinter4

def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        return f.read()

setup(
    name='pytest-splinter4',
    description='Pytest plugin for the splinter automation library',
    long_description=read('README.rst'),
    author='Joshua Fehler',
    license='MIT license',
    version=pytest_splinter4.__version__,
    include_package_data=True,
    url='https://github.com/jsfehler/pytest-splinter4',
    install_requires=[
        'splinter>=0.21.0',
        'pytest>=8.0.0',
        'webdriver_manager>=4.0.2',
    ],
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    extras_require={
        'dev': ['tox'],
    },
    entry_points={'pytest11': [
        'pytest-splinter4=pytest_splinter4.plugin',
    ]},
    packages=find_packages(),
)
