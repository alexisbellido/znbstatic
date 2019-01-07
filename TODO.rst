TODO
==============================================================================

Move notes to README when test and done.

Once the tests are ready use multi-stage build to remove ssh information from the image. 

Use setuptools to make distributable package.

Use examples from
requests
django-storages
django-static-version

--
Maybe I could also do

.. code-block:: bash

  $ export SSH_PRIVATE_KEY="$(cat ~/.ssh/id_rsa)"

and then use that environment variable to build with Dockerfile-2 without --build-arg.

.. code-block:: bash

  $ docker build -t alexisbellido/znbstatic-2 -f ./Dockerfile-2 .
---