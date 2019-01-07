znbstatic
=====================================================

Custom Django storage backend.

Features:

- Storage of assets managed by collectstatic on Amazon Web Services S3.
- Versioning using a variable from Django's settings (https://example.com/static/css/styles.css?v=1.2)

Installation Notes
------------------------------------------------------------------------------

Using a Docker container with some Python 3 packages for initial tests.

Change to the directory where the Dockerfile is and build the image from there. Note the use of $(date) to use today's date as part of the image's name.

.. code-block:: bash

  $ docker build --build-arg SSH_PRIVATE_KEY="$(cat ~/.ssh/id_rsa)" -t alexisbellido/znbstatic-$(date +%Y%m%d) .

Then run the container and make sure you don't map over the /root directory because that's where ssh key from the host is stored if you use a temporary container. 

.. code-block:: bash

  $ docker run -it --rm --mount type=bind,source=$PWD,target=/root/project alexisbellido/znbstatic-20190107:latest docker-entrypoint.sh /bin/bash