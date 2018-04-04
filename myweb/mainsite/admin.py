from django.contrib import admin

from .models import Iris

# Register your models here.

class IrisAdmin(admin.ModelAdmin):
    list_display = ("sepal_length","sepal_width","petal_length","petal_width","species")


admin.site.register(Iris,IrisAdmin)
