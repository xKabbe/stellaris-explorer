"""
File: setup.py
Author: Steven (Kabbe)
Description: Setup configuration for the Stellaris Explorer project

For more information, see: https://github.com/xKabbe/stellaris-explorer
"""
from setuptools import setup, find_packages

setup(
    name='stellaris-explorer',
    version='0.1.0',
    packages=find_packages(),
    author='Steven',
    description='User-friendly interface to explore and visualize exoplanet catalog data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xKabbe/stellaris-explorer',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)

