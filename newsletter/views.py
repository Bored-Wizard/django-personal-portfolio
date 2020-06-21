from django.shortcuts import render
from .models import NewsletterUsers
from django.conf import settings
from .forms import NewsletterUserSignupForm
from content.models import About, Social
from django.core.mail import send_mail
from django.contrib import messages

def newsletter_signup(request):
    form = NewsletterUserSignupForm(request.POST or None)
    social = Social
    about = About
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUsers.objects.filter(email=instance.email).exists():
            messages.warning(request, "Your Email Already Exist In Our Database", "alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(request, "Thanks For Subscribing To Our Newsletter", "alert alert-warning alert-dismissible" )
            subject = "Thank you for joining our newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            message = """Welcome to my Newsletter. To unsubscribe goto https://sujanbarman.pythonanywhere.com"""
            send_mail(subject,message,from_email,to_email,fail_silently=True)

    context = {
        'form' : form,
        'url': social,
        'profile': about,
    }

    return render(request,'NewsletterSignup.html',context)


def newsletter_unsubscribe(request):
    form = NewsletterUserSignupForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUsers.objects.filter(email=instance.email).exists():
            NewsletterUsers.objects.filter(email=instance.email).delete()
            messages.success(request, "You Have Been Unsubscribe To Our Newsletter", "alert alert-warning alert-dismissible" )
            subject = "Unsubscription confirmation"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            message = """You have been unsubscribed to our newsletter."""
            send_mail(subject,message,from_email,to_email,fail_silently=True)
        else:
            messages.warning(request, "Your Email  Desnt Already Exist In Our Database", "alert alert-warning alert-dismissible")


    context = {
        'form' : form,
    }

    return render(request,'NewsletterUnsubscribe.html',context)