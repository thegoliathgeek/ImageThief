from setuptools import setup
import sys

if sys.version_info < (3, 7):
    sys.exit('Sorry, Python < 3.7 is not supported')

VERSION = "1.1.0"

with open('README.rst', 'r') as f:
    long_description = f.read()
setup(
    name="ImageThief",
    version=VERSION,
    author="Dhanush",
    author_email="dhanushdazz@gmail.com",
    description="Get images from server running on default route",
    long_description=long_description,
    url="",
    packages=['ImageThief'],
    install_requires=["flask", "requests"],
    keywords=['raspberrypi', 'image-processing', 'image-getter'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
