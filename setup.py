import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-mailgun",
    version = "1.0.0",
    author = "Sebastian Lemery",
    author_email = "darkpicnic@gmail.com",
    description = "Django wrapper for Mailgun API",
    license = "BSD",
    keywords = "django mailgun",
    url = "http://packages.python.org/",
    packages=['mailgun'],
    long_description=read('README'),
    install_requires=[
        'requests>=0.13.7'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)