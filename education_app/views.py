from django.shortcuts import render, redirect
from .models import Word, Lesson
from .forms import WordForm, LessonForm


def home(request):
    """
    home page
    """
    return render(request, 'education_app/home.html')


def word_list(request):
    """
    word list
    """
    words = Word.objects.all()
    return render(request, 'education_app/word_list.html', {'words': words})


def word_add(request):
    """
    word add
    """
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = WordForm()
    return render(request, 'education_app/word_add.html', {'form': form})


def lesson_list(request):
    """
    lesson list
    """
    lessons = Lesson.objects.all()
    return render(request, 'education_app/lesson_list.html', {'lessons': lessons})


def lesson_add(request):
    """
    lesson add
    """
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForm()
    return render(request, 'education_app/lesson_add.html', {'form': form})
