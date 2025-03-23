from django import forms
from .models import Word, Lesson


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word_text', 'translation', 'image_url']

    def clean_word_text(self):
        data = self.cleaned_data['word_text']
        if len(data.strip()) == 0:
            raise forms.ValidationError("Поле слова не может быть пустым!")
        return data


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'words']
        widgets = {
            'words': forms.CheckboxSelectMultiple()
        }

    def clean_title(self):
        data = self.cleaned_data['title']
        if not data.strip():
            raise forms.ValidationError("Название урока не может быть пустым!")
        return data
