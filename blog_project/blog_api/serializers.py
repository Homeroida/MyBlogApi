# from rest_framework import serializers
# from .models import Post, Category


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


# class PostSerializer(serializers.ModelSerializer):
#     category_name = serializers.StringRelatedField(read_only=True)
#     author_username = serializers.SerializerMethodField()

#     class Meta:
#         model = Post
#         fields = '__all__'

#     def get_category_name(self, obj):
#         return obj.category.name if obj.category else None

#     def get_author_username(self, obj):
#         return obj.author.username if obj.author else None


from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(
    #     read_only=True)  # Display the category name
    # author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'
