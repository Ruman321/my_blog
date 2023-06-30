from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title        = models.CharField(max_length=200)
    content      = models.TextField()
    author       = models.ForeignKey(Author, on_delete=models.CASCADE)
    image        = models.ImageField(upload_to='post_images/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title