import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pelican_decorate_content",
    version="0.1.1",
    author="Frederik Ring",
    author_email="frederik.ring@gmail.com",
    description="A Pelican plugin for rule-based addition of classes to your content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/offen/pelican-decorate-content",
    packages=["pelican_decorate_content"],
    install_requires=["pelican>=3", "beautifulsoup4"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
