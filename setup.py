from setuptools import find_packages, setup

setup(
    name="dagstger_mflix",
    packages=find_packages(exclude=["dagstger_mflix_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
