from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'author']


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id', 'book_info', 'image']


class BookGetSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    author = serializers.CharField(source='author.author', read_only=True)

    class Meta:
        model = BookInfo
        fields = ['id',
                  'name',
                  'price',
                  'author',
                  'category',
                  'description',
                  'on_sale',
                  'isbn',
                  'language',
                  'type_of_lang',
                  'translator',
                  'num_of_pages',
                  'press',
                  'publish_date'
                  ]
        extra_kwargs = {
            'slug': {'read_only': True}
        }


class BookInfoSerializer(serializers.ModelSerializer):
    # book_image = BookImageSerializer(many=True)

    class Meta:
        model = BookInfo
        fields = ['id',
                  'name',
                  'price',
                  'author',
                  'category',
                  'description',
                  'on_sale',
                  'isbn',
                  'language',
                  'type_of_lang',
                  'translator',
                  'num_of_pages',
                  'press',
                  'publish_date'
                  ]
        extra_kwargs = {
            'slug': {'read_only': True}
        }


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['user', 'book_info', 'rate']
        extra_kwargs = {'user': {'required': False}}

    def create(self, attrs):
        user = self.context.get('request').user
        instance = Rate.objects.create(**attrs)
        instance.user = user
        instance.save()
        return instance
