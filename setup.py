# setup.py

from setuptools import setup, find_packages

setup(
    name="my_counter",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy"  # This will install numpy automatically as a dependency
    ],
    description="A simple counter module with increment, decrement, and randomize functions.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://example.com/my_counter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
