from django.contrib import admin
from .models import About, Work, Comments, Social, Googleapi


class AboutAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email')


class WorkAdmin(admin.ModelAdmin):
    list_display = ('name','work_url','workpic')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','profession')


class SocialAdmin(admin.ModelAdmin):
    list_display = ('facebook','github','instagram','likedin')


class GoogleapiAdmin(admin.ModelAdmin):
    list_display = ('googleapi')

admin.site.register(About, AboutAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Googleapi, GoogleapiAdmin)

