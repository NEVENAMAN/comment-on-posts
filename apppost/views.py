from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


def form_page(request):
    return render(request,'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        if request.method == "POST":
            Register(request)
        return redirect('/')

def login(request):
    if request.method == "POST":
        if Login(request):
            id = request.session['userid'] 
            user = User.objects.get(id=id)
            message = Get_message_info(request)
            comment = Get_comment_info(request)
            context = {
                "user" : user,
                 "messages" : message,
                 "comments" : comment,
            }
            return render(request,'wall.html',context)

    return redirect('/')

def wall_page(request):
    message = Get_message_info(request)
    comment = Get_comment_info(request)

    context = {
        "messages" : message,
        "comments" : comment,
    }
    return render(request,'wall.html',context)

def add_message(request):
    AddMessage(request)
    return redirect('/wall_page')

def add_comment(request):
    AddComment(request)
    return redirect('/wall_page')

