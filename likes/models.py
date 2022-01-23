import django
from django.db import models
from django.contrib.auth.models import User 
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# class Like(models.Model):
#     created_at = models.DateTimeField(auto_now=True)


class LikedItem(models.Model):
    #type of object(prodcut, video, article), id
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

