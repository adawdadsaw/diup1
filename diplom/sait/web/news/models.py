from django.db import models

class Artiles(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.CharField('Анонс', max_length=1000)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'