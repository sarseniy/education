from django.db import models


class Word(models.Model):
    word_text = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word_text


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    words = models.ManyToManyField(Word, related_name='lessons')  # связь с моделью Word
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
