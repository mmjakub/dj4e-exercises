from django.http.response import HttpResponse
from django.shortcuts import render

def index(req):
    num_visits = req.session.get('num_visits', 0) + 1
    req.session['num_visits'] = num_visits 
    if num_visits > 4 : del(req.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    resp.set_cookie('dj4e_cookie', '2b12fa2d', max_age=1000)
    return resp

def cookie(req):
    return HttpResponse('cookie')

def sessfun(req):
    visits = req.session.get('visit_count', 0)
    req.session['visit_count'] = visits + 1
    return HttpResponse(f'Seen you {visits} times before')
