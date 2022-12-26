from django.contrib import admin
from .models import *


class CardAdmin(admin.ModelAdmin):
    list_display = ('pretitle', 'title', 'content')
    list_display_links = ('pretitle', 'title', 'content')

admin.site.register(Card, CardAdmin)