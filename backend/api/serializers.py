from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "user", "category", "title", "description", "price", "photos", "quantity", "created_at", "updated_at"]
        read_only_fields = ["id", "user", "category", "created_at", "updated_at"]


class CategoryReadSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "description", "created_at", "updated_at", "posts"]
        read_only_fields = ["id", "created_at", "updated_at"]









class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_categories')
    name = models.CharField(max_length=100, null=False, blank=False, default="Раздел")
    description = models.CharField(max_length=1000, null=True, blank=False, default="Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'раздел объявлений'
        verbose_name_plural = 'разделы объявлений'

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, default="")
    price = models.IntegerField(default=0)
    photos = ArrayField(models.URLField(), blank=True, default=list)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

    def __str__(self):
        return self.title