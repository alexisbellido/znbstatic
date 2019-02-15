STATICFILES_STORAGE = 'znbstatic.storage.VersionedS3StaticStorage'
DEFAULT_FILE_STORAGE = 'znbstatic.storage.S3MediaStorage'

if get_env_variable('PROJECT_RUNNING_DEV') == 'true':
    # use this to test with IP
    #STATIC_URL = 'http://192.168.1.97:81/static/'
    #MEDIA_URL = 'http://192.168.1.97:81/media/'

    #STATIC_URL = 'http://example.com/static/'
    #MEDIA_URL = 'http://example.com/media/'

    # AWS S3
    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''
    AWS_STORAGE_STATIC_BUCKET_NAME = 'example-static-staging'
    AWS_STORAGE_MEDIA_BUCKET_NAME = 'example-media-staging'
    STATIC_URL = 'https://%s.s3.amazonaws.com:443/' % AWS_STORAGE_STATIC_BUCKET_NAME
    MEDIA_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_MEDIA_BUCKET_NAME

else:
    # AWS S3
    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''

    AWS_STORAGE_STATIC_BUCKET_NAME = 'example-static'
    AWS_STORAGE_MEDIA_BUCKET_NAME = 'example-media'

    # via AWS S3
    STATIC_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_STATIC_BUCKET_NAME
    MEDIA_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_MEDIA_BUCKET_NAME

    # via KeyCDN
    #STATIC_URL = 'https://%s.s3.amazonaws.com:443/' % AWS_STORAGE_STATIC_BUCKET_NAME
    #STATIC_CDN_URL = 'https://static-12345.kxcdn.com/'
    #MEDIA_URL = 'https://media-12345.kxcdn.com/'