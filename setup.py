from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    licenseFile = f.read()

setup(
    name='iyzipay',
    version='1.0.0',
    description='iyzipay api python client',
    long_description=readme,
    author='Iyzico',
    author_email='iyzico-ci@iyzico.com',
    url='https://github.com/iyzico/iyzipay-python',
    license=licenseFile,
    packages=find_packages(exclude=('tests', 'docs'))
)
