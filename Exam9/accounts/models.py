from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
from webapp.models import Photo, Album


class Profile(models.Model):
    favorites_photos = models.ManyToManyField(Photo, related_name='favorites_users', null=True,
                                              verbose_name="Избранные Фото")
    favorites_albums = models.ManyToManyField(Album, related_name='favorites_users', null=True,
                                              verbose_name="Избранные Альюомы")
    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE,
                                verbose_name="Пользователь",
                                related_name="profile")
