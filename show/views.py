# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response

def pigbloodcake(request):
        return render_to_response('pigbloodcake.html')
  
def alivetocopus(request):
        return render_to_response('alivetocopus.html')
  
def grasshopper(request):
        return render_to_response('grasshopper.html')  
  
def pigeon(request):
        return render_to_response('pigeon.html')  
  
def durian(request):
        return render_to_response('durian.html')  