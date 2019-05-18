
#!/usr/bin/env python
"""
Installs yourapp.
"""

from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='wagtail_guide',
      version='1',
      description='MY amazing app',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/coolperson/yourapp',
      author='Fox Mulder',
      author_email='fox.mulder@fbi.com',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      include_package_data=True,
      install_requires=[
          'wagtail>=2.4',
      ])
