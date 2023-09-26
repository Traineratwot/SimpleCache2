import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SimpleCache2",
    version="1.1.0",
    author="Traineratwot",
    author_email="Traineratwot@yandex.ru",
    description="Cache system for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/traineratwot/SimpleCache2",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)