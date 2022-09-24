from django.urls import path

from webapp.views.albums import AlbumView, CreateAlbum, UpdateAlbum, DeleteAlbum
from webapp.views.photos import IndexViewPhotos, PhotoView, CreatePhoto, UpdatePhoto, DeletePhoto

app_name = "webapp"

urlpatterns = [
    path('', IndexViewPhotos.as_view(), name="index"),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('photos/add/', CreatePhoto.as_view(), name="create_photo"),
    path('photo/<int:pk>/update/', UpdatePhoto.as_view(), name="update_photo"),
    path('photo/<int:pk>/delete/', DeletePhoto.as_view(), name="delete_photo"),
    path('album/<int:pk>/', AlbumView.as_view(), name='album_view'),
    path('album/add/', CreateAlbum.as_view(), name="create_album"),
    path('album/<int:pk>/update/', UpdateAlbum.as_view(), name="update_album"),
    path('album/<int:pk>/delete/', DeleteAlbum.as_view(), name="delete_album"),
]