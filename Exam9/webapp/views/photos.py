from uuid import uuid4

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

# Create your views here.
from django.utils.http import urlencode

from webapp.forms import PhotoForm, PhotoDeleteForm
from webapp.models import Photo, Album
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexViewPhotos(LoginRequiredMixin, ListView):
    model = Photo
    template_name = "photos/index.html"
    context_object_name = "photos"
    ordering = "-created_at"
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_private=False)
        return queryset


class PhotoView(LoginRequiredMixin, DetailView):
    template_name = "photos/photo_view.html"
    model = Photo
    context_object_name = "photo"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorite_users'] = self.object.favorites_users.all()
        return context

    # def has_permission(self):
    #     return super().has_permission() and self.request.user in self.get_object().users.all() or \
    #            super().has_permission() and self.request.user.groups.filter(name__in=("Moderator",)).exists()


class CreatePhoto(LoginRequiredMixin, CreateView):
    form_class = PhotoForm
    template_name = "photos/create.html"

    def form_valid(self, form):
        author = self.request.user
        form.instance.user = author
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial


class UpdatePhoto(PermissionRequiredMixin, UpdateView):
    form_class = PhotoForm
    template_name = "photos/update.html"
    model = Photo
    permission_required = "webapp.change_photo"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().user


class DeletePhoto(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = "photos/delete.html"
    success_url = reverse_lazy('webapp:index')
    form_class = PhotoDeleteForm
    permission_required = "webapp.delete_photo"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().user


class CreatePhotoToken(LoginRequiredMixin, UpdatePhoto):
    model = Photo
    form_class = PhotoDeleteForm

    def has_permission(self):
        return self.request.user == self.get_object().user

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def post(self, request, *args, **kwargs):
        object = self.get_object()

        if not object.token:
            token = uuid4().hex
            object.token = token
            object.save()

        return redirect('webapp:photo_view', pk=object.pk)


class PhotoTokenView(DetailView):
    template_name = "photos/photo_view.html"
    model = Photo
    context_object_name = "photo"

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        token = self.kwargs.get('token')
        try:
            obj = queryset.get(token=token)
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorite_users'] = self.object.favorites_users.all()
        return context
