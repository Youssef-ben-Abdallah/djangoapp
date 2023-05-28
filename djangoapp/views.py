from django.shortcuts import render
from django.template import loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def Home(request):
    return render(request, 'home.html' )