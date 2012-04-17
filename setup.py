import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pymigrate",
    version = "0.1",
    author = "Fang Nan",
    author_email = "nanfang05@gmail.com",
    description = ("Python code as data migrate scripts."),
    license = "BSD",
    keywords = "migrate migration",
    url = "http://packages.python.org/pymigrate",
    packages=['pymigrate'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        ],
)