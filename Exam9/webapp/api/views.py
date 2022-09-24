from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Photo, Album


class PhotoAddFavoriteView(APIView):

    def get(self, request, pk, *args, **kwargs):
        user = request.user
        photo = get_object_or_404(Photo, pk=pk)
        user.profile.favorites_photos.add(photo)
        return Response(status=status.HTTP_202_ACCEPTED)


class PhotoRemoveFavoriteView(APIView):

    def get(self, request, pk, *args, **kwargs):
        user = request.user
        photo = get_object_or_404(Photo, pk=pk)
        user.profile.favorites_photos.remove(photo)
        return Response(status=status.HTTP_202_ACCEPTED)


class AlbumAddFavoriteView(APIView):

    def get(self, request, pk, *args, **kwargs):
        user = request.user
        album = get_object_or_404(Album, pk=pk)
        user.profile.favorites_albums.add(album)
        return Response(status=status.HTTP_202_ACCEPTED)


class AlbumRemoveFavoriteView(APIView):

    def get(self, request, pk, *args, **kwargs):
        user = request.user
        album = get_object_or_404(Album, pk=pk)
        user.profile.favorites_albums.remove(album)
        return Response(status=status.HTTP_202_ACCEPTED)
