from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Mysetting




def index(request):
    settings=Mysetting.objects.get()
    contex={
        "settings":settings
    }
    return render(request,'pages/index.html',contex)
                