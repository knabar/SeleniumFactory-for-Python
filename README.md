SeleniumFactory for Python
---------------------------

This is a fork of https://github.com/mattfair/SeleniumFactory-for-Python.  No functionality has been added, but the files have been reorganized into a `pip` installable package.

Simple interface factory to create Selenium objects, inspired by SeleniumFactory interface 
from https://github.com/infradna/selenium-client-factory.

The main objective is to be able to have an automatic interface to easily run tests under the Bamboo Sauce Ondemand plugin as well as local tests.  The factory object reads environments variables setup by the Bamboo plugin and creates a remote Sauce OnDemand session accordingly, otherwise it creates a local selenium configuration.

For selenium 2 webDriver:

    from pyseleniumfactory import SeleniumFactory
    webDriver = SeleniumFactory().createWebDriver()

For selenium 1 RC:

    from pyseleniumfactory import SeleniumFactory
    browser = SeleniumFactory().create()


