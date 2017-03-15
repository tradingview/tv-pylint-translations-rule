from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='pylint-translations-rule',

    version='0.0.1',

    url='https://github.com/pypa/sampleproject',

    author='Igor Emets',
    author_email='iemets@nwork.local',

    license='MIT',

    packages=find_packages(),

    install_requires=['pylint'],

    # $ pip install -e .test
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },
)