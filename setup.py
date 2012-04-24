import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pymigrate",
    version = "0.1",
    author = "Fang Nan",
    author_email = "nanfang05@gmail.com",
    description = ("Pymigrate is a tool for you to use python scripts or whatever self runnable scripts as your migration sripts for your data and systme."),
    license = "BSD",
    keywords = "python migrate migration",
    url = "http://github.com/nanfang/pymigrate",
    packages=['pymigrate',],
    long_description=read('README.rst'),
    scripts=['scripts/pymigrate'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)