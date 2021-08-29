from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_blog")
    blog_title = models.CharField(max_length=400, verbose_name="Put A Title")
    slug = models.SlugField(max_length=200, unique=True)
    blog_content = models.TextField(verbose_name="What's On Your Mind?")
    blog_image = models.ImageField(
        upload_to="blog_images", verbose_name="Image" null="True", blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.blog_title




