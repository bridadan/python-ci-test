import os
from distutils.core import setup
from io import open
from setuptools import find_packages

DESCRIPTION = "Test Python module"
OWNER_NAMES = "Brian Daniels"
OWNER_EMAILS = "brianddaniels@gmail.com"


# Utility function to cat in a file (used for the README)
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="utf8").read()

setup(name='mymodule',
      version='0.0.1',
      description=DESCRIPTION,
      long_description=read('README.md'),
      author=OWNER_NAMES,
      author_email=OWNER_EMAILS,
      maintainer=OWNER_NAMES,
      maintainer_email=OWNER_EMAILS,
      url='https://github.com/bridadan/python-ci-test',
      packages=find_packages(),
      license="Apache-2.0",
      test_suite = 'test',
      tests_require = [
          "mock>=2"
      ]
)
