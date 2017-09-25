from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.name }}",
    version="0.1dev",
    packages=find_packages(),
    install_requires=[],
    description="{{ cookiecutter.description }}",
    long_description=open('README.txt').read(),
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    url="{{ cookiecutter.url }}",
    license="{{ cookiecutter.license }}",
    classifiers=[]
)
