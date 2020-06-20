from django.contrib import admin
from .models import NewsletterUsers

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','created_at')

admin.site.register(NewsletterUsers, NewsletterAdmin)