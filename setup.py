import os

from setuptools import find_packages, setup

with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'requests >= 0.8.8',
]

setup(
    name='iyzipay',
    version='1.0.40',
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
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
