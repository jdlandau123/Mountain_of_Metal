from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    publish_date = models.DateTimeField(default = timezone.now)
    body = models.TextField()
    image = models.ImageField(blank = True, upload_to = 'images')
    slug = models.SlugField(null = True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class ContactFormModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=500)
    cc_myself = models.BooleanField(default=True)
