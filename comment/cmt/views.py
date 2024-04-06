from django.shortcuts import render
from rest_framework import viewsets
from .models import Comment
from .serializer import CommentSerializer


class CommnetHandleView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
