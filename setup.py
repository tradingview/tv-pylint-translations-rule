import sys

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

if sys.version_info[0] < 3:
    version_dependent_requirements = ['astroid==1.4.9', 'pylint==1.6.5']
else:
    version_dependent_requirements = ['pylint>=2.3.1,<3.0', 'astroid>=2.2.5,<3.0']

setup(
    name='pylint-translations-rule',

    version='0.0.4',

    url='https://github.com/pypa/sampleproject',

    author='Igor Emets',
    author_email='iemets@nwork.local',

    license='MIT',

    packages=find_packages(),

    install_requires=[
        'pytest==3.0.7',
        'six',
    ] + version_dependent_requirements,
)
