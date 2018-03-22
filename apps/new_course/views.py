# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from models import *

def index(request):
    all_courses = Course.objects.all()  
    context = {
        'all_courses' : all_courses
    }
    return render(request, 'new_course/index.html', context)

def add_course_process(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        name = request.POST['name']
        desc = request.POST['desc']
        add = Course.objects.create(name = name, desc = desc)
        add.save()
        return redirect('/')

def destroy(request, course_id):
    course = Course.objects.get(id = course_id)
    context = {
        'course' : course
    }
    return render(request, 'new_course/destroy_page.html', context)

def delete_course_process(request):
    course_id = request.POST['course_id']
    if 'No' in request.POST:
        return redirect('/')
    if 'Yes' in request.POST:
        d = Course.objects.get(id = course_id)
        d.delete()
        return redirect('/')
    