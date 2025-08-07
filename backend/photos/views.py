from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import AllowAny

from .models import Post

from .serializers import (
    PostSerializer
)

from .permissions import PhotoIsAdminOrDebugOrReadOnly


class PhotosView(RetrieveUpdateDestroyAPIView):
    permission_classes = [PhotoIsAdminOrDebugOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = 'post_id'
    http_method_names = ['get', 'patch', 'delete']
    def get_object(self):
        queryset = self.get_queryset()
        category_id = self.kwargs.get("category_id")
        post_id = self.kwargs.get("post_id")
        obj = get_object_or_404(queryset, pk=post_id, category__id=category_id)
        self.check_object_permissions(self.request, obj)
        return obj
    
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)