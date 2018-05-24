from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='pylint-translations-rule',

    version='0.0.4',

    url='https://github.com/pypa/sampleproject',

    author='Igor Emets',
    author_email='iemets@nwork.local',

    license='MIT',

    packages=find_packages(),

    install_requires=[
        'astroid==1.4.9',
        'pylint==1.6.5',
        'pytest==3.0.7',
        'six',
    ],
)
