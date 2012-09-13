import os
import sys
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-mailgun',
    version='1.0.0',
    packages=['mailgun'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description="A Django wrapper for the Mailgun API",
    long_description=read('README'),
    keywords='django mailgun',
    author='Sebastian Lemery',
    author_email='darkpicnic@gmail.com',
    install_requires=[
           'requests >= 0.13.7',
        ],
)