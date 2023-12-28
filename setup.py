from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

version_dependent_requirements = []

setup(
    name='pylint-translations-rule',
    version='0.0.4',
    url='https://github.com/pypa/sampleproject',
    author='Igor Emets',
    author_email='iemets@nwork.local',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pylint>=3.0',
        'astroid>=3.0'
    ]
)
