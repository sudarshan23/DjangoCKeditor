from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime

# Create your models here.
class Post(models.Model):

    #fields of the model
    body = RichTextUploadingField(blank=True)
    created = models.DateTimeField(default=datetime.now)
