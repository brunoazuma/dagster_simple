from setuptools import find_packages, setup

setup(
    name="blob_storage",
    packages=find_packages(exclude=["blob_storage_tests"]),
    install_requires=[
        "dagster"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
