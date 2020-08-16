import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "spelltest",
    version = "0.0.2",
    author = "bidipeppercrap",
    author_email = "bidipeppercrap@outlook.com",
    description = "SPELL TEST mechanics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bidipeppercrap/spelltest.py",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires = ">=3.8",
)
