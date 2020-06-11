from django.shortcuts import render
from .models import About, Work, Comments, Social


def home(request):
    about = About.objects.all()
    works = Work.objects.all()
    comments = Comments.objects.all()
    social = Social.objects.all()
    return render(request, 'main.html', {
        'about': about,
        'works': works,
        'comments': comments,
        'social': social,
    })