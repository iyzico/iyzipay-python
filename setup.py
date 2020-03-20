import os
import sys
import warnings

from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = []

if sys.version_info < (2, 6):
    warnings.warn(
        'Python 2.5 is not officially supported by iyzico. '
        'If you have any questions, please open an issue on Github or '
        'contact us at integration@iyzico.com.',
        DeprecationWarning)
    install_requires.append('requests >= 0.8.8, < 0.10.1')
    install_requires.append('ssl')
else:
    install_requires.append('requests >= 0.8.8')

setup(
    name='iyzipay',
    version='1.0.37',
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'future'],
    description='iyzipay api python client',
    long_description=README,
    author='iyzico',
    author_email='iyzico-ci@iyzico.com',
    url='https://github.com/iyzico/iyzipay-python',
    license=LICENSE,
    packages=find_packages(exclude='tests'),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
