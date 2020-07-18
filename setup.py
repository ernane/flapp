from setuptools import find_packages, setup


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="flapp",
    version="0.1.0",
    description="Template application with Flask",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")},
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov", "pytest-flask"],
    python_requires=">=3.6",
)
