from django.contrib import admin
from .models import FileUpdate

class FileUpdateAdmin(admin.ModelAdmin):
    pass

admin.site.register(FileUpdate, FileUpdateAdmin)
