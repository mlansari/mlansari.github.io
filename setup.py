"""Setup for the site"""
from setuptools import setup

setup(
    name='mlansari',
    packages=['mlansari'],
    include_package_data=True,
    install_requires=[
        'flask'
    ],
)