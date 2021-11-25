from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False,null=False,blank=False)
    slug = models.SlugField(null=True,blank=True)
    class Meta:
        verbose_name = 'My Blog'
        verbose_name_plural = 'My Blogs'

    def __str__(self):
        return self.title
