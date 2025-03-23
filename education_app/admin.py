from django.contrib import admin
from .models import Word, Lesson


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('word_text', 'translation', 'timestamp')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
