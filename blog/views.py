# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, 'blog/index.html', {})


def acc_login(request):
    print (request.POST)
    err_msg = ''
    if request.method == "POST":
        print ('user authentication')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request.user)  # generate session id
            return HttpResponseRedirect('/')
        else:
            err_msg = 'wrong username or password'

    return render(request, 'blog/index.html', {'err_msg': err_msg})

class acc_registerview(TemplateView):
    template_name = 'blog/main_page.html'

    def post(self, request):
        print('username': )


