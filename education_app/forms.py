from django import forms
from .models import Word


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word_text', 'translation', 'image_url']

    def clean_word_text(self):
        data = self.cleaned_data['word_text']
        if len(data.strip()) == 0:
            raise forms.ValidationError("Поле слова не может быть пустым!")
        return data
