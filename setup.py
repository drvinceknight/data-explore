from setuptools import setup, find_packages

setup(
    name="dataexplorer",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
)
