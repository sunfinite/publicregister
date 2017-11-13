# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from publicregister import utils as u
import os
import time

def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    elif request.method == 'POST':
        if request.POST.get('add_submit'):
            return add(request)
        else:
            return verify(request)

def save_file(f):
   file_name = os.path.join(settings.BASE_DIR, 'publicregister', 'uploads', 
      '%f_%s' % (time.time(), f.name))
   with open(file_name, 'wb+') as fout:
        for chunk in f.chunks():
            fout.write(chunk)
   return file_name

def add(request):
   if request.method == 'POST':
      if request.POST['passphrase'] == 'apple':
         file_name = save_file(request.FILES['file'])
         s = u.detect_text(file_name)
         tx_id = u.add_entry(s)
         return render(request, 'main.html',  
            {'message': "Hashes successfully recorded on the blockchain: %s"
               % tx_id, 'class': 'info'})
      else:
         return render(request, 'main.html',
            {'message': "Invalid passphrase", 'class': 'danger'})

def verify(request):
    if request.method == 'POST':
        file_name = save_file(request.FILES['file'])
        s = u.detect_text(file_name)
        is_valid = u.verify_entry(s)
        if is_valid:
            message = "Valid marks card!"
            class_ = "success"
        else:
            message = "Invalid marks card!"
            class_ = "danger"
   
    return render(request, 'main.html',
        {'message': message, 'class': class_})
