from django.urls import path
from .views import *
app_name='bookinfo'
urlpatterns=[
    path('category-list/',CategoryListApi.as_view()),
    path('category-create/',CategoryCreateApi.as_view()),
    path('author-list/', AuthorListAPIView.as_view()),
    path('author-create/', AuthorCreateAPIView.as_view()),
    path('book-info-list/', BookInfoListAPIView.as_view()),
    path('book-info-create/', BookInfoCreateAPIView.as_view()),
    path('book-info/<int:pk>/', BookInfoRetrieveUpdateAPIView.as_view()),
    path('book-info-destroy/<int:pk>/', BookInfoDestroyAPIView.as_view()),
]
