# DjangoCKeditor
Basic Implementation of CK Editor in Django to convert the Text to HTML using WYSISYG !


Add below lines in your main settings.

    #CKEditor #START
    'txt2htm.apps.Txt2HtmConfig',
    'ckeditor',
    'ckeditor_uploader',
    #CKEditor #STOP
    
CKEDITOR_UPLOAD_PATH = 'uploads/'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
