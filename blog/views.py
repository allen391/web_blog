# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


# def index(request):
#     return render(request, 'blog/index.html', {})


def acc_login(request):
    print (request.POST)
    err_msg = ''
    if request.method == "POST":
        print ('user authentication')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # generate session id
            return HttpResponseRedirect('/blog/index/')
        else:
            err_msg = 'wrong username or password'

    return render(request, 'blog/index.html', {'err_msg': err_msg})

class acc_registerView(TemplateView):
    template_name = 'blog/register.html'

    def post(self, request):
        pass
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username)
        print(password)
        print(email)
        if User.objects.filter(username=username).exists():
            return HttpResponse("用户名已存在")
        user = User.objects.create_user(
            username, email, password)
        # login(request,  user)
        return HttpResponseRedirect('/blog/login/')
        return HttpResponse("注册成功")
        # print('username': )


class MainPageView(TemplateView):
    template_name = 'blog/main_page.html'

    # def get_template_names(self):
    #     if self.request.is_mobile:
    #         return 'blog/mobile/main_page.html'
    #     if self.request.is_pc:
    #         return 'blog/pc/main_page.html'
