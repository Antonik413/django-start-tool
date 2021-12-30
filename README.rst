=================
django-start-tool
=================

Introduction
------------

django-start-tool is a full-featured replacement for
``django-admin startproject`` which provides cli for creating the same
django project structure.

Usage
-----

A cli arguments are the same as startproject_ arguments excluding the several 
changes.

.. _startproject: https://docs.djangoproject.com/en/4.0/ref/django-admin/#startproject

-t --template
~~~~~~~~~~~~~

Changes:

- Creating from archive only supports the **zip** archive.

- Creating from remote source only supports the **GitHub** repositories.

----

-f --files
~~~~~~~~~~

This parameter is a replacement for ``--extension`` and ``--name`` parameters.

It takes space-separated glob patterns, like ``*.env *.rst Procfile`` etc.

----

--extra
~~~~~~~

This parameter takes space-separated key value pairs, which will be available 
in Jinja2 template from ``extra`` object.

.. code-block:: console

    $ django-start \
    > -t https://github.com/user/repository/archive/main.zip \
    > -f '*.env' \
    > -e 'db_name=mydb db_password=secret!' \
    > config .

``.env``:

.. code-block:: sh

    DB_NAME='{{ extra.db_name }}'
    DB_PASSWORD='{{ extra.db_password }}'

    # Will be rendered to
    DB_NAME='mydb'
    DB_PASSWORD='secret!'

License
-------

This package is distributed under the MIT license.
