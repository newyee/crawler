import os, sys
from setuptools import setup, find_packages

def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

setup(
    packages=['get_response'],
    name='get_response',
    version='0.0.1',
    description='get response for Crawling',
    author='Shinya',
    author_email='shinya33001@gmail.com',
    install_requires=read_requirements(),
    url='https://github.com/newyee/get_response',
    license='MIT',
)