from django.contrib import admin

from cinema import models


# Register your models here.

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


class SeanceAdmin(admin.TabularInline):
    model = models.Seance
    extra = 1


@admin.register(models.Film)
class FilmAdmin(admin.ModelAdmin):
    inlines = [SeanceAdmin]
