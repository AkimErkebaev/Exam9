from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

# Create your views here.
from django.utils.http import urlencode

from webapp.forms import PhotoForm, PhotoDeleteForm, AlbumForm, AlbumDeleteForm
from webapp.models import Photo, Album
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class AlbumView(DetailView):
    template_name = "albums/album_view.html"
    model = Album
    context_object_name = "album"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = self.object.photos.filter(is_private=False)
        return context

    # def has_permission(self):
    #     return super().has_permission() and self.request.user in self.get_object().users.all() or \
    #            super().has_permission() and self.request.user.groups.filter(name__in=("Moderator",)).exists()


class CreateAlbum(LoginRequiredMixin, CreateView):
    form_class = AlbumForm
    template_name = "albums/create.html"

    def form_valid(self, form):
        author = self.request.user
        form.instance.user = author
        return super().form_valid(form)


class UpdateAlbum(PermissionRequiredMixin, UpdateView):
    form_class = AlbumForm
    template_name = "albums/update.html"
    model = Album
    permission_required = "webapp.change_album"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().user


class DeleteAlbum(PermissionRequiredMixin, DeleteView):
    model = Album
    template_name = "albums/delete.html"
    success_url = reverse_lazy('webapp:index')
    form_class = AlbumDeleteForm
    permission_required = "webapp.delete_album"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().user