faker_web
=========

 |pypi| |unix_build| |coverage| |license|

faker_web is a provider for the `Faker`_ Python package.

It provides web-related fake data for testing purposes:

   * Content-type http header.
   * Popular web server version tokens/signatures.


Usage
-----

Install with pip:

.. code:: bash

    pip install faker_web

Or install with setup.py

.. code:: bash

    git clone https://github.com/thiagofigueiro/faker_web.git
    cd faker_web && python setup.py install

Add the ``WebProvider`` to your ``Faker`` instance:

.. code:: python

    from faker import Faker
    from faker_web import WebProvider

    fake = Faker()
    fake.add_provider(WebProvider)

    fake.content_type()
    # application/mxf
    fake.content_type_popular()
    # text/html
    fake.server_token()
    # Apache/2.0.51 (Ubuntu)


.. |pypi| image:: https://img.shields.io/pypi/v/faker_web.svg?style=flat-square&label=version
    :target: https://pypi.python.org/pypi/faker_web
    :alt: Latest version released on PyPi

.. |unix_build| image:: https://img.shields.io/travis/thiagofigueiro/faker_web/master.svg?style=flat-square&label=unix%20build
    :target: http://travis-ci.org/thiagofigueiro/faker_web
    :alt: Build status of the master branch on Mac/Linux

.. |coverage| image:: https://img.shields.io/coveralls/thiagofigueiro/faker_web/master.svg?style=flat-square
    :target: https://coveralls.io/r/thiagofigueiro/faker_web?branch=master
    :alt: Test coverage

.. |license| image:: https://img.shields.io/badge/license-apache-blue.svg?style=flat-square
    :target: https://github.com/thiagofigueiro/faker_web/blob/master/LICENSE
    :alt: Apache license version 2.0

.. _Faker: https://github.com/joke2k/faker
