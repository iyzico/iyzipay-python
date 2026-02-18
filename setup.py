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
    version='1.0.45',
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'future'],
#    description='iyzipay api python client',
#    long_description=README,
    long_description="Test Description",
    author='iyzico',
    author_email='iyzico-ci@iyzico.com',
    url='https://github.com/iyzico/iyzipay-python',
#    license=LICENSE,
    license="MIT",
    packages=find_packages(exclude='tests'),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
