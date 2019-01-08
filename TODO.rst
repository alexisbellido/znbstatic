TODO
==============================================================================

make sure all needed files are copied to project's python path, try pushing to git and then pip installing from there into a separate empty python project, when done try removing from example main Django project and add it there first via git and then from requirements file using PyPI, which will require making package distributable there

Move notes to README when test and done.

Once the tests are ready use multi-stage build to remove ssh information from the included Dockerfile. 

--
I might use an environment variable to pass an ssh private key to the intermediate Docker image for development.

.. code-block:: bash

  $ export SSH_PRIVATE_KEY="$(cat ~/.ssh/id_rsa)"

and then use that environment variable to build with Dockerfile-2 without --build-arg.

.. code-block:: bash

  $ docker build -t alexisbellido/znbstatic-2 -f ./Dockerfile-2 .

copy documentation to add to Django settings

add the following to INSTALLED_APPS

'znbstatic.apps.ZnbStaticConfig'

and make sure these two are also there
  'storages'
  'django.contrib.staticfiles'

add context processor to the correspoding template engine 'znbstatic.context_processors.static_urls'

...

# STATICFILES_STORAGE = 'znbstatic.storage.VersionedStaticFilesStorage'
# STATIC_URL = '/static/'

STATICFILES_STORAGE = 'znbstatic.storage.VersionedS3StaticFilesStorage'

AWS_ACCESS_KEY_ID = 'AKIAIE123456VNM5QLRA'
AWS_SECRET_ACCESS_KEY = 'W8N123MzsMrq7Lb123FRYpNjjYj4WVJoYsy7kvjE'

AWS_STORAGE_STATIC_BUCKET_NAME = 'static.example.com'
AWS_S3_HOST = 's3.amazonaws.com'
S3_USE_SIGV4 = True
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = 'public-read'
STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_STATIC_BUCKET_NAME

ZNBSTATIC_VERSION = '0.1'