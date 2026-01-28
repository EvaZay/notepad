#описание структуры данных(модели)
from django.db import models

'''
класс описания модели заметки
class Note(models.Model)
'''
class Note(models.Model):
    #заголовок заметки
    title = models.CharField(max_length=100)
    #текст заметки
    body = models.TextField()
    #дата создания
    created_at = models.DateTimeField(auto_now_add=True)
    '''
    метод, который возвращает строковое значение
    def __str__(self)
    '''
    def __str__(self):
        #отображение в админке
        return self.title

