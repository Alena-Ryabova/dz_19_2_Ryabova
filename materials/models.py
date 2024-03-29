from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blogpost(models.Model):
    post_name = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=200, verbose_name='URL')
    blog_content = models.TextField(verbose_name='содержимое', **NULLABLE)
    blog_preview = models.ImageField(upload_to='post_images/', verbose_name='превью', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True)
    publication_indicator = models.BooleanField(default=True, verbose_name='признак публикации')
    count_of_views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} {self.post_name} {self.slug} {self.created_at} '

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
