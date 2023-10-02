from django.http.response import HttpResponse
from django.shortcuts import render

def index(req):
    return HttpResponse('index')

def cookie(req):
    return HttpResponse('cookie')

def sessfun(req):
    return HttpResponse('sessfun')
