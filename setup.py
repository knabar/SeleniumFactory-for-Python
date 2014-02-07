from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pyseleniumfactory',
      version=version,
      description="SeleniumFactory for Python",
      long_description="""\
Simple interface factory to create Selenium objects, inspired by SeleniumFactory interface from https://github.com/infradna/selenium-client-factory.  The main objective is to be able to have an automatic interface to easily run tests under the Bamboo Sauce Ondemand plugin as well as local tests.  The factory object reads environments variables setup by the Bamboo plugin and creates a remote Sauce OnDemand session accordingly, otherwise it creates a local selenium configuration.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='selenium python factory seleniumfactory',
      author='Andreas Knab',
      author_email='knabar@gmail.com',
      url='https://github.com/knabar/pyseleniumfactory',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "selenium",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
