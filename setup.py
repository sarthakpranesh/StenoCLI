import setuptools
from io import open
from os import path

with open("README.md", "r") as fh:
    long_description = fh.read()

import pathlib
HERE = pathlib.Path(__file__).parent

# automatically captured required modules for install_requires in requirements.txt and as well as configure dependency links
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
    install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (not x.startswith('#')) and (not x.startswith('-'))]
    dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setuptools.setup(
    name="stenocli", # Replace with your own username
    version="0.0.1",
    author="Sarthak Pranesh",
    author_email="limphned@gmail.com",
    description="Perform Image and Text Steganography from your terminal!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarthakpranesh/StenoCLI",
    packages=setuptools.find_packages(),
    install_requires = install_requires,
    dependency_links=dependency_links,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    entry_points={
        "console_scripts": [
            "stenocli=StenoCLI.__main__:main",
        ]
    },
)