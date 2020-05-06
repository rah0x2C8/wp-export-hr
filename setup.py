import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wp-export-hr",
    version="0.0.1",
    author="rah0x2C8",
    author_email="64735511+rah0x2C8@users.noreply.github.com",
    description="Parse WordPress export to human readable format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rah0x2C8/wp-export-hr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
