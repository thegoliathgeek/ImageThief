from setuptools import setup


VERSION = "2.0.1"

with open('README.rst', 'r') as f:
    long_description = f.read()
setup(
    name="ImageThief",
    version=VERSION,
    author="Dhanush",
    author_email="dhanushdazz@gmail.com",
    description="Get files from server running on default route",
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
