abc-server
==========

.. image:: https://travis-ci.org/esikachev/abc-server.svg?branch=master
    :target: https://travis-ci.org/esikachev/abc-server


**How to run**

1. Run command 
.. sourcecode:: console

    $ tox -e venv -- abc-server -e <email> -p <password> 
..

email and password from github.

2. Send REST request like:

.. sourcecode:: console

    $ curl -H "Content-Type: application/json" -X POST -d '{"files": ["~/.bash_profile"]}' http://127.0.0.1:5000/add
..
