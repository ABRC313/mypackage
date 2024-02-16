from setuptools import setup, find_packages


setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license="MIT",
    description= "test project",
    long_description=open('README.md').read(),
    requires=['numpy']
)