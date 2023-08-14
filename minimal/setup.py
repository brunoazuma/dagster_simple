from setuptools import find_packages, setup

setup(
    name="minimal",
    packages=find_packages(exclude=["minimal_tests"]),
    install_requires=[
        "dagster"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
