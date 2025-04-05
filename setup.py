from setuptools import setup, find_packages

setup(
    name="mcpsec",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "PyNaCl>=1.5.0",
        "jsonschema>=4.0.0",
    ],
    python_requires=">=3.7",
    description="Model Context Protocol Security SDK for Python",
    author="Mantas Insurance Solutions, Inc.",
    license="Apache 2.0",
)
