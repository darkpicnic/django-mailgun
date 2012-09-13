from setuptools import setup, find_packages

setup(
    name='django-mailgun',
    version='1.0.0',
    packages=['mailgun'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description="A Django wrapper for the Mailgun API",
    long_description=open('README.md').read(),
    author_email='darkpicnic@gmail.com',
    install_requires=[
           'requests >= 0.13.7',
        ],
)