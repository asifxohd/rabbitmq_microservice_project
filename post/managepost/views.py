from rest_framework import viewsets ,status
from .models import Posts
from .serializers import PostsSerializer
from rest_framework.response import Response


class PostviewController(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('comments')  
        return queryset
