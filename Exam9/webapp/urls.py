from django.urls import path

from webapp.api.views import PhotoAddFavoriteView, AlbumAddFavoriteView, PhotoRemoveFavoriteView, \
    AlbumRemoveFavoriteView
from webapp.views.albums import AlbumView, CreateAlbum, UpdateAlbum, DeleteAlbum
from webapp.views.photos import IndexViewPhotos, PhotoView, CreatePhoto, UpdatePhoto, DeletePhoto, CreatePhotoToken, \
    PhotoTokenView

app_name = "webapp"

urlpatterns = [
    path('', IndexViewPhotos.as_view(), name="index"),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('photos/add/', CreatePhoto.as_view(), name="create_photo"),
    path('photo/<int:pk>/update/', UpdatePhoto.as_view(), name="update_photo"),
    path('photo/<int:pk>/delete/', DeletePhoto.as_view(), name="delete_photo"),
    path('photo/<int:pk>/create_token/', CreatePhotoToken.as_view(), name="create_photo_token"),
    path('photo/<str:token>/', PhotoTokenView.as_view(), name="photo_view_token"),
    path('album/<int:pk>/', AlbumView.as_view(), name='album_view'),
    path('album/add/', CreateAlbum.as_view(), name="create_album"),
    path('album/<int:pk>/update/', UpdateAlbum.as_view(), name="update_album"),
    path('album/<int:pk>/delete/', DeleteAlbum.as_view(), name="delete_album"),
    path('favorite/add/photo/<int:pk>/', PhotoAddFavoriteView.as_view(), name="add_favorite_photo"),
    path('favorite/add/album/<int:pk>/', AlbumAddFavoriteView.as_view(), name="add_favorite_album"),
    path('favorite/remove/photo/<int:pk>/', PhotoRemoveFavoriteView.as_view(), name="remove_favorite_photo"),
    path('favorite/remove/album/<int:pk>/', AlbumRemoveFavoriteView.as_view(), name="remove_favorite_album"),
]
