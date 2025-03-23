from django.shortcuts import render, redirect
from .models import Word
from .forms import WordForm


def home(request):
    return render(request, 'education_app/home.html')


def word_list(request):
    words = Word.objects.all()
    return render(request, 'education_app/word_list.html', {'words': words})


def word_add(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = WordForm()
    return render(request, 'education_app/word_add.html', {'form': form})
