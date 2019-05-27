from rest_framework import viewsets
from blog.serializer import BlogSerializer
from blog.models import Blog


class BlogViewSet(viewsets.ModelViewSet):

    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
