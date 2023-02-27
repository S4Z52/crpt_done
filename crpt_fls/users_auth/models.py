from django.db import models
from django import forms
from django.contrib.auth.models import User


class FileUp (models.Model):
    file_name = models.TextField()
    file_upper = models.FileField(upload_to='images/')

    def __str__(self):
        return self.file_name
