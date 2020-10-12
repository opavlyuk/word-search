from setuptools import setup


setup(
    name="word-search",
    # packages=["ltf2.util"],
    version="0.0.1",
    description="Search fow words in pre-generated 2d grid",
    author="Oleksandr Pavliuk",
    author_email="pavlyuk.olexandr@gmail.com",
    python_requires=">=3.6.10",
    url="https://github.com/opavlyuk/word-search",
    entry_points={
        "console_scripts": ["word-search = src.main:main"],
    },
)