from django.db import models

from main.models import User


class Admin(models.Model):
  name = models.CharField(max_length=120, unique=True)
  email = models.EmailField()

  def __str__(self):
      return self.name


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120, primary_key=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    admin = models.ForeignKey('Admin', related_name='admins', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post', null=True, blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}: {self.text}"

