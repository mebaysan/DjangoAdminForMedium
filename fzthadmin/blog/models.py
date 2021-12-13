from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, null=False, blank=False)
    slug = models.SlugField(null=True, blank=True)
    category = models.ManyToManyField(to='blog.Category', related_name='blogs')
    class Meta:
        verbose_name = 'My Blog'
        verbose_name_plural = 'My Blogs'

    def __str__(self):
        return self.title

    @property
    def get_when_was_created(self):
        return (timezone.now() - self.added_date).days


class Comment(models.Model):
    blog = models.ForeignKey(
        to='blog.Blog', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    added_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'

    def __str__(self):
        return f"{self.blog.title} - {self.content}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'

    def __str__(self):
        return self.name





