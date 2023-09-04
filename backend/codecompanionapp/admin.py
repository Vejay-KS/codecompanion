from django.contrib import admin
from .models import Codecompaniontest

class CodeCompanionTestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Codecompaniontest, CodeCompanionTestAdmin)