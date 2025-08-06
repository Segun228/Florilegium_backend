from django.urls import path
from photos.views import (
    PhotosUploadView
)


urlpatterns = [
    path('photos/upload/', PhotosUploadView.as_view(), name='post-list-create'),
]