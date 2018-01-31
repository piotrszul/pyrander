from setuptools import setup 
setup(
  name = 'pyranderx',
  packages = ['pyrander'], # this must be the same as the name above
  version = '0.0.2',
  description = 'A random test lib',
  author = 'Piotr Szul',
  author_email = 'piotr.szul@csiro.au',
  url = 'https://github.com/piotrszul/pyrander',
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
  extras_require = {
    'test': [ 
      'pyspark==2.1.2', 
    ],
  },
  license = "MIT",
)
