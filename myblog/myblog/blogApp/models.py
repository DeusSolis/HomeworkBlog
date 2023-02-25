from django.db import models

from django.utils.text import slugify


class CategoryModel(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class PostModel(models.Model):
    name = models.CharField(max_length=64)
    content = models.TextField()
    slug = models.SlugField(max_length=64, blank=True, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_column="created")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated")
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post'
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
