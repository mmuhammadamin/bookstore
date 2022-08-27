from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from .serializers import *
from ..users.permissions import IsAdminUserForAccount


class CategoryListApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryCreateApi(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserForAccount]


class AuthorCreateAPIView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUserForAccount]


class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookInfoListAPIView(generics.ListAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookGetSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserForAccount]
    filter_backends = (SearchFilter,)

    def get_queryset(self):
        qs = super().get_queryset().filter(is_deleted=False)
        search = self.request.GET.get('search')
        cat = self.request.GET.get('cat')
        author = self.request.GET.get('author')
        if search:
            qs = qs.filter(name__icontains=search)
        if cat:
            qs = qs.filter(category__name=cat)
        if author:
            qs = qs.filter(author__author=author)
        return qs


class BookInfoCreateAPIView(generics.CreateAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    permission_classes = [IsAdminUserForAccount]


class BookInfoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class BookInfoDestroyAPIView(generics.DestroyAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    permission_classes = (IsAdminUserForAccount,)
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.is_deleted = True
