=======================
substanced-cookiecutter
=======================

A cookiecutter (project template) for creating a Substance D starter project.

Requirements
------------

* Python 2.7 or 3.3+
* `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_

Usage
-----

1. Generate a Substance D project.

.. code-block:: bash

    $ cookiecutter https://github.com/Pylons/substanced-cookiecutter

2. Change directory to the project name given in the last cookiecutter question.

.. code-block:: bash

    $ cd my_project_name

3. Run your project.

.. code-block:: bash

    $ bin/pserve development.ini

For Python 3, a virtual environment is automatically created and set up in development mode.
