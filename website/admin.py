from django.contrib import admin
from .models import Question,Python,Solved

# Register your models here.
admin.site.register(Question)
admin.site.register(Python)
admin.site.register(Solved)
