from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


STATUS = ((0, 'Draft'), (1, 'Published'))


class Reviews(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='review_post')
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    body = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
