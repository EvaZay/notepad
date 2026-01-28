#функции и классы, которые отвечают на запросы
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from .forms import NoteForm
from .models import Note

'''
метод, отображающий список всех заметок
def notes_list(request)
    request - объект запроса
'''
def notes_list(request):
    #получение всех заметок
    notes = Note.objects.all()
    #возвращаем HTML-шаблон с данными
    return render(request, 'notes/index.html', {'notes': notes})
'''
метод, отображающий детали одной заметки
def note_detail(request, note_id)
    request - объект запроса
    note_id - id заметки
'''
def note_detail(request, note_id):
    #получаем заметки по id или возвращаем 404
    note = get_object_or_404(Note, pk=note_id)
    #возвращаем HTML-шаблон с данными
    return render(request, 'notes/detail.html', {'note': note})

'''
метод для создания заметки
def note_create(request)
    request - объект запроса
'''
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():  #Валидация данных
            form.save()
            return redirect('notes_list')  #Редирект после сохранения
    else:
        form = NoteForm()
    return render(request, 'notes/form.html', {'form': form, 'title': 'Создать заметку'})

'''
метод для редактирования заметки
def note_edit(request, note_id)
    request - объект запроса
    note_id - id заметки
'''
def note_edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', note_id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/form.html', {'form': form, 'title': 'Редактировать заметку'})

'''
метод удаления заметки с подтверждением 
@require_http_methods(["GET", "POST"]) - защита: разрешён только GET и POST

def note_delete(request, note_id):
    request - объект запроса
    note_id - id заметки
'''
@require_http_methods(["GET", "POST"])
def note_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        note.delete()
        return redirect('notes_list')

    return render(request, 'notes/confirm_delete.html', {'note': note})