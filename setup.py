from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'distobjects',
  packages = find_packages(),
  version = '0.0.1a1',
  license='GPLv3',
  description = 'Python library to easily map Objects to Caching Systems like Redis',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url = 'https://github.com/svrdev27/py-distobjects',
  download_url = 'https://github.com/svrdev27/py-distobjects/archive/v0.0.1-alpha.1.tar.gz',
  keywords = ['redis', 'ODM', 'distributed objects', 'caching'],
  install_requires=[
          'redis'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
