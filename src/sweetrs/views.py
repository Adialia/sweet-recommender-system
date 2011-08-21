from django.contrib.auth.models import User
from django.views.generic.simple import direct_to_template
from recommender.models import Rating
from django.shortcuts import redirect
import django

__author__ = 'kidzik'

def about(request):
    """ list products """
    context = {
        'users': User.objects.all().count(),
        'ratings': Rating.objects.all().count(),
        'usersbar': User.objects.all().count(),
        'ratingsbar': Rating.objects.all().count() / 20,
    }
    return direct_to_template(request, 'flatpages/about.html', extra_context=context)

def logout(request):
    django.contrib.auth.logout(request)
    return redirect('about_us')