import pathlib
from setuptools import setup, find_packages

ROOT_DIR = pathlib.Path(__file__).parent

README = (ROOT_DIR / "README.md").read_text()

setup(
    name="poem_parser",
    version="0.0.1",
    description="Parse poems into stressed and unstressed syllables",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/obeezzy/poem_parser",
    author="Chronic Coder",
    author_email="efeoghene.obebeduo@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=["prosodic"],
)
