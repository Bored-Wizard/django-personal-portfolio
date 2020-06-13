from django.shortcuts import render
from .models import About, Work, Comments, Social


def home(request):
    about = About.objects.all()[0]
    works = Work.objects.all()
    comments = Comments.objects.all()
    social = Social.objects.all()[0]
    return render(request, 'main.html', {
        'profile': about,
        'works': works,
        'comments': comments,
        'url': social,
    })