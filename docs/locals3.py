STATICFILES_STORAGE = 'znbstatic.storage.VersionedS3StaticStorage'
DEFAULT_FILE_STORAGE = 'znbstatic.storage.S3MediaStorage'

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_STATIC_BUCKET_NAME = 'example-static-staging'
AWS_STORAGE_MEDIA_BUCKET_NAME = 'example-media-staging'
AWS_STORAGE_PRIVATE_BUCKET_NAME = 'example-private-staging'
STATIC_URL = 'https://%s.s3.amazonaws.com:443/' % AWS_STORAGE_STATIC_BUCKET_NAME
MEDIA_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_MEDIA_BUCKET_NAME