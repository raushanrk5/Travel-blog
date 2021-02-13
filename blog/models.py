from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60)
    category_slug = models.SlugField(unique=True, max_length=100, default=1)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.category_slug:
            self.category_slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,  verbose_name="Writer")
    title = models.CharField(max_length=200, verbose_name="Title")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    article_image = models.ImageField(upload_to='images/', verbose_name="Add image", null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=100)
    categories = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_date']
