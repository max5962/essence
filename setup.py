import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = ""

# This call to setup() does all the work
setup(
    name="PrixCarburantClient",
    version="1.0.1",
    description="StationEssence client ",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/max5962/essence",
    author="Maxime Wantiez",
    author_email="",
    license="MIT",
    packages=["prixCarburantClient"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)
