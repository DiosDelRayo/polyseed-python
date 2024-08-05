from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()
    f.close()

with open("LICENSE.txt", "r") as f:
    license = f.read()
    f.close()

setup(
    name="polyseed",
    version="0.2.1",
    author="DiosDelRayo",
    author_email="no@spam",
    description="A Python module for polyseed, compatible with https://github.com/tevador/polyseed.git",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DiosDelRayo/polyseed-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
    license=license
)
