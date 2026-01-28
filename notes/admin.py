#регистрация моделей в админке
from django.contrib import admin
from .models import Note

admin.site.register(Note)