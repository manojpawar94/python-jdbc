import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-jdbc",
    version="0.0.1",
    author="Manoj Pawar",
    author_email="mmpawar94@gamil.com",
    description="It is an abstraction to execute jdbc queries with minimal code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manojpawar94/python-jdbc",
    project_urls={
        "Bug Tracker": "https://github.com/manojpawar94/python-jdbc/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
