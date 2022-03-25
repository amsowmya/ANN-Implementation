from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
setup(
    name="src",
    version="0.0.2",
    author="sowmya",
    description="A small package for ANN implimentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amsowmya/ANN-Implementation",
    author_email="soumya.pdit@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "tensorflow",
        "pandas",
        "numpy",
        "seaborn",
        "matplotlib"
    ]
)