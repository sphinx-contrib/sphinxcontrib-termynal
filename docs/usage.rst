Usage
=====

**termynal** usage documentation.

Installation
------------

Install **termynal** directly from pypi using pip:

.. code-block::

    pip install sphinxcontrib-termynal

To activate the extension you must add it to your ``conf.py`` file:

.. code-block:: python

    # docs/conf.py

    extensions = [
        ...
        "sphinxcontrib.termynal",
        ...
    ]

Usage
-----

Here we demonstrate how one could display the **termynal** roles directives.

demo-directive
^^^^^^^^^^^^^^

The package is providing a ``demo-directive``:

.. tab-set::

    .. tab-item:: rst

        .. code-block:: reStructuredText

            .. demo-directive:: This is a demo directive.

    .. tab-item:: MyST

        .. code-block:: md

            ```{demo-directive} This is a demo directive.
            ```

And here is the result :

.. demo-directive:: This is a demo directive.

demo-role
^^^^^^^^^

The package is providing a ``demo-role``:

.. tab-set::

    .. tab-item:: reStructuredText

        .. code-block:: rst

            I'm an :demo-role:`demo` role.

    .. tab-item:: MyST

        .. code-block:: md

            I'm an {demo-role}`demo` role.

And here is the result :

I'm an :demo-role:`demo` role.
