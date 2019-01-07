znbstatic
=====================================================

Custom Django storage backend.

Features:

- Storage of assets managed by collectstatic on Amazon Web Services S3.
- Versioning using a variable from Django's settings (https://example.com/static/css/styles.css?v=1.2)

Installation Notes
------------------------------------------------------------------------------

Change to the directory where the Dockerfile is and build the image from there.

.. code-block:: bash

  $ docker build --build-arg SSH_PRIVATE_KEY="$(cat ~/.ssh/id_rsa)" -t alexisbellido/znbstatic-$(date +%Y%m%d) .
