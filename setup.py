from setuptools import setup
from . import __version__, __author__, __license__

setup(name='pydevrant',
      version=__version__,
      description='Python wrapper the DevRant API',
      url='https://github.com/Olamyy/pydevrant',
      author=__author__,
      author_email='olamyy53@gmail.com',
      license=__license__,
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=['requests'],
      packages=['pydevrant'],
      zip_safe=False
      )
