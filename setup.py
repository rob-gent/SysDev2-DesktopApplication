import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DesktopApplication-rmg226",
    version="0.0.1",
    author="Robson Gent",
    author_email="rmg226@exeter.ac.uk",
    description="A prototype desktop application for online sellers using E-Bay and other online shopping services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rob-gent/SysDev2-DesktopApplication.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: Creative Commons Zero v1.0 Universal",
        "Operating System :: Windows 10 installations",
    ],
    python_requires='>=3.6',
)