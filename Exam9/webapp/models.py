from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.urls import reverse


class Photo(models.Model):
    photo = models.ImageField(upload_to="image", null=False, blank=False, verbose_name='Фотография')
    signature = models.CharField(max_length=250, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="photos",
                             verbose_name='Автор')
    album = models.ForeignKey('webapp.Album', related_name="photos", null=True, blank=True, verbose_name='Альбом',
                              on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)
    token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.pk}'

    def get_absolute_url(self):
        return reverse("webapp:photo_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "photos"
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Album(models.Model):
    name = models.CharField(max_length=250, verbose_name='Навзвание')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="albums",
                             verbose_name='Автор')
    is_private = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("webapp:album_view", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = "albums"
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
